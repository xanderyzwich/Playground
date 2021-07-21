// Reverse an array in place

export function reverse_array(input_arr: number[]){
    const end = input_arr.length-1
    const halfway = Math.floor(end/2)
    for (var i = 0; i < halfway; i++) {
        var temp = input_arr[i]
        input_arr[i] = input_arr[end-i]
        input_arr[end-i] = temp
    }
    return
}

