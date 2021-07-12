// Reverse an array in place

function reverse_array(input_arr: number[]){
    const end = input_arr.length-1
    const halfway = Math.floor(end/2)
    for (var i = 0; i < halfway; i++) {
        var temp = input_arr[i]
        input_arr[i] = input_arr[end-i]
        input_arr[end-i] = temp
    }
    return
}

function test_reverse_array() {
    let data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    console.log(data)
    reverse_array(data)
    console.log(data)

    data = [1, 2, 3, 4, 5, 6, 7, 8]
    console.log(data)
    reverse_array(data)
    console.log(data)
}
