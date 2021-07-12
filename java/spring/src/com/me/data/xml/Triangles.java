package com.me.data.xml;

import java.util.List;

public class Triangles {
    private List<Triangle> triangles;

    public Triangles() {
    }

    public Triangles(List<Triangle> triangles) {
        this.triangles = triangles;
    }

    public List<Triangle> getTriangles() {
        return triangles;
    }

    public void setTriangles(List<Triangle> triangles) {
        this.triangles = triangles;
    }

    public void print(){
        for (Triangle t : triangles){
            t.print();
        }
    }
}
