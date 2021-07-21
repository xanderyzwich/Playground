// Write a function that finds the missing number in an unsorted array containing every one of the other 99 numbers ranging from 1 to 100.
import {bubble_sort} from "./bubble_sort";
import generate from "./generate";

export function find_missing(input_arr: number[]) : number {
    let count = input_arr.length + 1
    let data : number[] = generate(count)
    let sorted_arr = input_arr
    bubble_sort(sorted_arr)

    // console.log("Enter find_missing")
    // console.log("  " + count + " : " + input_arr)
    // console.log("  " + sorted_arr)
    // console.log("  " + data)
    var output
    for (var i = 0; i < count; i++) {
        // console.log("Comparing[" + i + "] " + sorted_arr[i] + " and " + data[i])
        if ( sorted_arr[i] != data[i]){
            return data[i]
        }
    }
    return 0
}