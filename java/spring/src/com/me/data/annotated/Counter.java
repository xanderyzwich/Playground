package com.me.data.annotated;

import org.springframework.stereotype.Component;

import javax.annotation.Resource;

@Component
@Resource(name="counter")
public class Counter {
    private int count;


    public Counter() { this.count = 0;    }
    public int getCount() { return ++this.count;    }

    @Override
    public String toString(){
        return "Counter { " +
                "next count=" + (this.count + 1) +
                " }";
    }

}
