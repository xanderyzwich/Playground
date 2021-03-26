package com.me.data.annotated;

import com.me.beans.DisplayNameBeanPostProcessor;
import org.springframework.context.annotation.*;

@Configuration
@EnableAspectJAutoProxy
@ComponentScan({"com.me.data.annotated", "com.me.aspect"})
@PropertySource(value="classpath:/com/me/properties/my.properties")
public class ThingConfiguration {

//    @Bean(name = "counter")
//    public Counter getCounter(){
//        return new Counter();
//    }

//    @Bean(name = "singletonThing")
//    @Scope("singleton")
//    public Thing getThing(){
//        return  new Thing();
//    }

//    @Bean(name = "prototypeThing")
//    @Scope("prototype")
//    public ThingPrototype getPrototypeThing(){
//        return new ThingPrototype();
//    }

    @Bean(name = "otherThingPrototype")
    @Scope("prototype")
    public OtherThing getPrototypeThing(){
        OtherThing ot =  new OtherThing();
        ot.setDescription("from configuration");
        return ot;
    }

    @Bean
    public DisplayNameBeanPostProcessor getDisplayNameBeanPostProcessor(){
        return new DisplayNameBeanPostProcessor();
    }
}
