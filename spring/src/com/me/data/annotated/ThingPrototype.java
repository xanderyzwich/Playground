package com.me.data.annotated;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

@Component("prototypeThing")
@Scope("prototype")
public class ThingPrototype extends Thing {
    public ThingPrototype() {
        super();
    }

    @Autowired
    public void setDescription(@Value("from java") String description){
        this.description = description;
    }
}
