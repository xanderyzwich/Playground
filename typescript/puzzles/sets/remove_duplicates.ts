// Write a function that removes every duplicate value in an array.

// import bubble_sort from "./bubble_sort"

// There could be more than one value duplicated. You should remove all of them leaving a single copy of the value.

export function remove_duplicates(input_arr:number[]) :number[] {
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