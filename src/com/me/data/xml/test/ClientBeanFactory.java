package com.me.data.xml.test;

import com.me.data.xml.Triangle;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.FileSystemResource;

public class ClientBeanFactory {
    public static void main(String[] args) {
        BeanFactory factory = new XmlBeanFactory(new FileSystemResource(("src/context.xml")));
        Triangle triangle = (Triangle) factory.getBean("triangle");
        triangle.print();
    }
}
