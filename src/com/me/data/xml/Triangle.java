package com.me.data.xml;


import org.springframework.beans.factory.BeanNameAware;

public class Triangle implements BeanNameAware {
    private Point one;
    private Point two;
    private Point three;
    private String beanName;

    public Triangle() {
    }

    public Triangle(Point one, Point two, Point three) {
        this.one = one;
        this.two = two;
        this.three = three;
    }

    @Override
    public String toString() {
        return "Triangle{ " +
                "one=" + one +
                ", two=" + two +
                ", three=" + three +
                "} " + this.beanName;
    }

    public Point getOne() {
        return one;
    }

    public void setOne(Point one) {
        this.one = one;
    }

    public Point getTwo() {
        return two;
    }

    public void setTwo(Point two) {
        this.two = two;
    }

    public Point getThree() {
        return three;
    }

    public void setThree(Point three) {
        this.three = three;
    }

    public void print(){
        System.out.println(toString());
    }

    @Override
    public void setBeanName(String beanName) {
        this.beanName = beanName;

    }
}
