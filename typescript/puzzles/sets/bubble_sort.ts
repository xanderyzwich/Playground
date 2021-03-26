// sort array of numbers in place

function bubble_sort(input_arr: number[]) {
    do {
        var is_ordered = true
        for (var i = 0; i < input_arr.length; i++) {
            if(input_arr[i+1] < input_arr[i]) {
                [input_arr[i], input_arr[i+1]] = [input_arr[i+1], input_arr[i]]
                is_ordered = false
            }
        }
    }
    while(!is_ordered);
}

function test_bubble_sort() {
    let data : number[] = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    console.log("Before: " + data)
    bubble_sort(data)
    console.log("After : " + data)
}

export default bubble_sort;