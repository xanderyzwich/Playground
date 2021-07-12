package com.me.data.xml.test;

import com.me.data.xml.Thing;
import com.me.data.xml.Triangles;
import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class ClientApplicationContext {
    public static void main(String[] args) {
        AbstractApplicationContext context = new ClassPathXmlApplicationContext("com/me/data/xml/context.xml");
        context.registerShutdownHook();
//        Triangle triangle= (Triangle) context.getBean("triangle"); // using ref
//        Triangle triangle= (Triangle) context.getBean("triangle-inner"); // using inner beans
//        triangle.print();
        Triangles triangles= (Triangles) context.getBean("triangles");
        triangles.print();

        System.out.println();
        for(int i = 0; i < 10; i++){
//            System.out.println("Thing One:");
            Thing thing1 = (Thing) context.getBean("thingOne");
//            thing1.print();
        }

        System.out.println();
        for(int i = 0; i < 10; i++){
//            System.out.println("Thing Two:");
            Thing thing2 = (Thing) context.getBean("thingTwo");
//            thing2.print();
        }

        System.out.println();
        for(int i = 0; i < 10; i++){
//            System.out.println("Thing Two:");
            Thing annotatedThing1 = (Thing) context.getBean("annotatedThing1");
//            thing2.print();
        }
        System.out.println();
        for(int i = 0; i < 10; i++){
//            System.out.println("Thing Two:");
            Thing annotatedThing2 = (Thing) context.getBean("annotatedThing2");
//            thing2.print();
        }

    }
}
