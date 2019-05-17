package com.me.beans;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.stereotype.Component;

@Component
public class DisplayNameBeanPostProcessor implements BeanPostProcessor {

    @Override
    public Object postProcessBeforeInitialization(Object bean, String name) throws BeansException {
//        System.out.println("Entering " + bean.getClass() + " named: " + name + " looks like: " + bean.toString());
        String packageName = bean.getClass().getPackage().getName();
        return bean;
    }

    @Override
    public Object postProcessAfterInitialization(Object bean, String name) throws BeansException {
        System.out.println(name + " looks like: " + bean.toString());
        return bean;
    }

}
