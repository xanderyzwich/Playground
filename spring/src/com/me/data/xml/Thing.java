package com.me.data.xml;

import org.springframework.beans.factory.BeanNameAware;

public class Thing implements BeanNameAware {
    private int id;
    private Counter counter;
    private String beanName;

    public Thing() {
    }

    public Thing(Counter counter) {
        this.id = counter.getCount();
    }
    public Thing(int id){
        this.id = id;
        System.out.println("created by int id");
    }


    @Override
    public String toString() {
        return "Thing{" +
                "id=" + this.id +
                "} " +this.beanName;
    }

    public void print(){
        System.out.println(toString());
    }

    public Counter getCounter() {
        return counter;
    }

    public void setCounter(Counter counter) {
        this.counter = counter;
    }

    @Override
    public void setBeanName(String beanName) {
        this.beanName = beanName;
    }
}
