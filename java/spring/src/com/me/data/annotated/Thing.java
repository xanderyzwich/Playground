package com.me.data.annotated;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import javax.annotation.Resource;

@Component("singletonThing")
@Scope("singleton")
public class Thing {

    protected int id;
    protected String description;

    @Resource(name="counter")
    private Counter counter;

    public Thing() { return;    }

    @Autowired
    public void setDescription(@Value("${def-thing}") String description){
        this.description = description;
    }

    @PostConstruct
    public void setup(){
        this.id = counter.getCount();
//        System.out.print("PostConstruct called on " + this.getClass().getSimpleName());
    }

    @Override
    public String toString(){
        return this.getClass().getSimpleName() +" { " +
                "id=" + this.id +
                ", description = " + this.description +
                " }";
    }

    public void print(){
        System.out.println(this.toString());
    }

}
