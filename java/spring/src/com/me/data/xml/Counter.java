package com.me.data.xml;

import org.springframework.beans.factory.DisposableBean;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.beans.factory.annotation.Required;
import org.springframework.stereotype.Component;

@Component("counter")
public class Counter implements InitializingBean, DisposableBean {


    private int count;

    public Counter() {
        this.count = 0;
    }
    public Counter(int seed){
        this.count = seed;
    }

    @Required
    public void setCount(int count){
        this.count = count;
    }

    public int getCount(){
        this.count += 1;
        return this.count;
    }

    @Override
    public void afterPropertiesSet() throws Exception {
        System.out.println(" - Counter has been created! count:" + this.count);
    }

    @Override
    public void destroy() throws Exception {
        System.out.println(" - Counter is being destroyed with final count of " + this.count);
    }
}
