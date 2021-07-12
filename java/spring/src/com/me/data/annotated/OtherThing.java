package com.me.data.annotated;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component("otherThing")
public class OtherThing {

    @Value("#{counter.getCount()}")
    private int id;

    private String description = "not configured yet";

    public OtherThing(){    }

    public void setDescription(@Value("${def-thing}") String description) {
        this.description = description;
    }

    @Override
    public String toString(){
        return "OtherThing { " +
                "id = " + this.id +
                ", description = " + this.description +
                " }";
    }

    public void print(){
        System.out.println(this.toString());
    }

}
