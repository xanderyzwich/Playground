package com.me.data.xml.test;

import com.me.data.xml.Point;
import com.me.data.xml.Triangle;

public class Client {
    public static void main(String[] args) {
        Point one = new Point(0, 0 );
        Point two = new Point(1, 0 );
        Point three = new Point(0, 1 );

        Triangle triangle = new Triangle(one, two, three);
        triangle.print();
    }
}
