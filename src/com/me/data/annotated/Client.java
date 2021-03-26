package com.me.data.annotated;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;


public class Client {
    public static void main(String[] args) {
//        ApplicationContext ac = new ClassPathXmlApplicationContext("com/me/data/annotated/spring.xml");
        ApplicationContext ac = new AnnotationConfigApplicationContext(ThingConfiguration.class);
        Logger logger = LogManager.getLogger(Client.class);

        System.out.println();
        for(int i = 0; i < 3; i++){
            Thing thing1 = (Thing) ac.getBean("singletonThing", Thing.class);
            logger.warn("Thing One: " + thing1.toString());
        }

        System.out.println();
        for(int i = 0; i < 3; i++){
            Thing annotatedThing = (Thing) ac.getBean("prototypeThing", ThingPrototype.class);
            logger.warn("Thing Two: " + annotatedThing.toString());
         }

        System.out.println();
        for(int i = 0; i < 3; i++){
            OtherThing prototypeOtherThing = (OtherThing) ac.getBean("otherThingPrototype", OtherThing.class);
            logger.warn("Thing Two: " + prototypeOtherThing.toString());
        }


        ((AnnotationConfigApplicationContext)ac).close();
    }
}
