package com.me.data.annotated;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;


public class Client {
    public static void main(String[] args) {
//        ApplicationContext ac = new ClassPathXmlApplicationContext("com/me/data/annotated/spring.xml");
        ApplicationContext ac = new AnnotationConfigApplicationContext(ThingConfiguration.class);

        System.out.println();
        for(int i = 0; i < 3; i++){
//            System.out.println("Thing One:");
            Thing thing1 = (Thing) ac.getBean("singletonThing", Thing.class);
            thing1.print();
        }

        System.out.println();
        for(int i = 0; i < 3; i++){
//            System.out.println("Thing Two:");
            Thing annotatedThing = (Thing) ac.getBean("prototypeThing", ThingPrototype.class);
//            annotatedThing.print();
        }

        System.out.println();
        for(int i = 0; i < 3; i++){
//            System.out.println("Thing Two:");
            OtherThing prototypeOtherThing = (OtherThing) ac.getBean("otherThingPrototype", OtherThing.class);
//            prototypeOtherThing.print();
        }

//        Log log = (Log) ac.getBean(Log.class);



        ((AnnotationConfigApplicationContext)ac).close();
    }
}
