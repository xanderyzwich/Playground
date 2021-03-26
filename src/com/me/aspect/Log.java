package com.me.aspect;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.Signature;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

import java.util.Arrays;
import java.util.stream.Collectors;

@Component
@Aspect
public class Log {

    Logger logger = LogManager.getLogger(Log.class);
    String before = "Incoming  :: ";
    String after  = "Completed :: ";
    
    @Before("execution(* com.me.data.annotated..*(..))")
    public void log(JoinPoint jp){
        Signature signature = jp.getSignature(); // who is called "class method"
        logger.debug(before  + signature.toShortString() + " : " + joinArgs(jp));
    }

    @AfterReturning(
            pointcut = "execution(* com.me.data.annotated.*.*(..)) && !execution(String *.toString(..))" ,
            returning= "retVal")
    public void methodLog(JoinPoint jp, Object retVal){
        String methodCall = jp.getSignature().toShortString() ;
        String logString = after + methodCall + " [ args = " +joinArgs(jp) + " ]";
        if (retVal != null) {
            logString += " return =  " + retVal.toString();
        }
        logger.info(logString);
    }

    private String joinArgs(JoinPoint jp){
        return Arrays.stream(jp.getArgs())
                .map(t -> t.toString())
                .collect(Collectors.joining(", "));
    }
}
