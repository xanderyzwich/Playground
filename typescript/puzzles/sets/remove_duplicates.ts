// Write a function that removes every duplicate value in an array.

import bubble_sort from "./bubble_sort"

// There could be more than one value duplicated. You should remove all of them leaving a single copy of the value.

function remove_duplicates(input_arr:number[]) :number[] {
    let max = Math.max(...input_arr)
    let output_arr = new Array()
    for (let i = 0; i < input_arr.length; i++) {
        let val = input_arr[i]
        if (output_arr.indexOf(val) < 0) {
            output_arr.push(val)
        }
    }
    return output_arr
}

function test_remove_duplicates() {
    let data = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 7, 9]
    console.log("Testing remove_duplicate on " + data + " Result: " + remove_duplicates(data))
}
test_remove_duplicates()

export default remove_duplicates