package com.fedex.cds.corey.strings;

import java.util.HashMap;
/*
*	Created for defining a dynamic list of properties
*	Origin was to define different requirements for included fields for same request
*/
public class PropertyMapper{
	private HashMap <String,String> map = new HashMap <String,String> ();
	
	/*
	 * This constructor allows a map of key,value pairs from a single property file line
	 * designed to allow for more dynamic usage of properties without code change
	 */
	PropertyMapper(String propertiesString, String splitChars){
		map = makeSimpleMap(propertiesString,splitChars);
	}
	
	/*
	 * Call constructor using only the output from the toString
	 */
	PropertyMapper(String propertiesString){
		this(propertiesString, ",=");
	}
	
	public boolean setProperty(String key, String value){
		if (map.keySet().contains(key))	{
			map.put(key,value);
			return true;
		}else return false;
	}
	
	public String getProperty(String key){
		return map.get(key);
	}
	
	public String toString(){
		String temp = new String("");
		for ( String k : map.keySet()){
			temp.concat(k +"=" +map.get(k) +',');
		}
		return temp.substring(0, temp.length()-1);
	}
		
	/*
	*	This is the internal method for splitting a string based on a single char
	*		splitString("property=value","="); 
	*		returns String[] {"property", "value"}
	*/
	private static String[] splitString(String in, String splitChar){
		return in.split(splitChar);
	}
	
	/*	chars is expected to have length = 2 (returns null otherwise)
	*		makeSimpleMap("prop1=1;prop2=2;prop3=3",";="); 
	*		returns HashMap{"prop1","1"; 
	*				"prop2","2"; 
	*/				"prop3","3"}
	private static HashMap<String,String> makeSimpleMap(String in, String splitChars){
		if (splitChars.length() != 2) return null;
		HashMap<String,String> tempMap = new HashMap<String,String>();
		String[] tempKeyValues = in.split(splitChars.substring(0, 1));
		for (String s : tempKeyValues){
			String[] entry = splitString(s,splitChars.substring(1,2));
			tempMap.put(entry[0], entry[1]);
		}
		return tempMap;
	}
}
