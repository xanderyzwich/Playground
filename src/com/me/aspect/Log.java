package com.me.aspect;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.Signature;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

import java.util.Arrays;
import java.util.stream.Collectors;

@Component
@Aspect
public class Log {

    @Before("execution(* com.me.data.annotated..*(..))")
    public void log(JoinPoint jp){
//        System.out.println(jp.toShortString());

        Object[] args = jp.getArgs(); // args
        String argString = Arrays.stream(args).map(t -> t.toString()).collect(Collectors.joining(", "));

        Signature signature = jp.getSignature(); // who is called "class method"
        JoinPoint.StaticPart staticPart = jp.getStaticPart(); // execution....
        System.out.println("   ::   " + signature.toShortString() + " : " + argString  );
    }
}
