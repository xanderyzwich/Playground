// sort array of numbers in place

export function bubble_sort(input_arr: number[]) {
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