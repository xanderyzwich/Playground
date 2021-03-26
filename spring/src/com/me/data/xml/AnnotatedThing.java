package com.me.data.xml;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import javax.annotation.Resource;

public class AnnotatedThing extends Thing{

    @Resource(name="counter")
    private Counter counter;

    private int id;

    private String description;

    public AnnotatedThing() {}

    @Autowired
    public void setDescription(@Value("This bean was configured with annotations") String description) {
        this.description = description;
    }

    @Override
    public String toString() {
        return "AnnotatedThing{" +
                "id=" + this.id +
                "description=" + this.description +
                "} ";
    }

    @PostConstruct
    public void initialize(){
        this.id = this.counter.getCount();
        System.out.println(this.getClass() + " has been created");
    }

    @PreDestroy
    public void destructor(){
        System.out.println(this.getClass() + " has been destroyed");
    }
}
