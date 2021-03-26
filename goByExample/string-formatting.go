package main

import (
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func main() {
	p := point{1, 2}
	fmt.Printf("%v\n", p)
	fmt.Printf("%+v\n", p) // Include field names from struct
	fmt.Printf("%#v\n", p) // Inlude Go syntax representation
	fmt.Printf("%T\n", p)  // The Type

	fmt.Printf("%t\n", true)  // bool format

	fmt.Printf("%d\n", 123)   //standard base-10
	fmt.Printf("%b\n", 14)    //binary
	fmt.Printf("%c\n", 33)    //character
	fmt.Printf("%x\n", 456)   //hex
	fmt.Printf("%f\n", 78.9)  //basic float
	fmt.Printf("%e\n", 123400000.0) //different float formats
	fmt.Printf("%E\n", 123400000.0)


	fmt.Printf("%s\n", "\"string\"") //basic string print
	fmt.Printf("%q\n", "\"string\"") //doublequoted strings to match source
	fmt.Printf("%x\n", "hex this")   //hex characters with two output chars per byte of input
	fmt.Printf("%p\n", &p)               //pointer

	fmt.Printf("|%6d|%6d|\n", 12, 345)         //fixed width
	fmt.Printf("|%6.2f|%6.2f|\n", 1.2, 3.45)   //fixed width with float format
	fmt.Printf("|%-6.2f|%-6.2f|\n", 1.2, 3.45) //left justified
	fmt.Printf("|%6s|%6s|\n", "foo", "b")      //string fixed width
	fmt.Printf("|%-6s|%-6s|\n", "foo", "b")    //now right justified

	s := fmt.Sprintf("a %s", "string") // same functionality of Printf without printing
	fmt.Println(s)

	fmt.Fprintf(os.Stderr, "an %s\n", "error") // printing to io.Writers

}
