package com.me.data.xml;

public class Point {
    private int x;
    private int y;

    public Point() {
    }

    public Point(int x, int y){
        setX(x);
        setY(y);
    }

    public int getX() { return x; }
    public void setX(int x) { this.x = x; }

    public int getY() { return y; }
    public void setY(int y) { this.y = y; }

    public String toString(){
        return "(" + x + ", " + y + ")";
    }

    public void print(){
        System.out.println(toString());
    }

    public void myInit(){
        System.out.println(" - Point " +  toString() + " has been created!");

    }

    public void myDestroy(){
        System.out.println(" - Point " + toString() + " has been destroyed!");
    }
}
