package com.me.beans;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.stereotype.Component;

@Component
public class DisplayNameBeanPostProcessor implements BeanPostProcessor {

    Logger logger = LogManager.getLogger(DisplayNameBeanPostProcessor.class);
    String before = "Entering  :: ";
    String after  = "Completed :: ";

    @Override
    public Object postProcessBeforeInitialization(Object bean, String name) throws BeansException {
        logger.debug(before + bean.getClass() + " named: " + name + " looks like: " + bean.toString());
//        String packageName = bean.getClass().getPackage().getName();
        return bean;
    }

    @Override
    public Object postProcessAfterInitialization(Object bean, String name) throws BeansException {
        logger.info(after + name + " : " + bean.toString());
        return bean;
    }

}
