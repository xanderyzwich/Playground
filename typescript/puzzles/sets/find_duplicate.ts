// Write a function that finds the duplicate number in an unsorted array containing every number from 1 to 100.
// Only one of the numbers will appear twice.

function find_duplicate(input_arr:number[]) : number {
    let count : number = input_arr.length - 1
    let found = Array(count)
    for (let i = 0; i < input_arr.length; i++) {
        let val = input_arr[i]
        if (found[val] === true) {
            return val
        }
        found[input_arr[i]] = true
    }
    return 0
}

function test_find_duplicate(){
    let data : number[] = [1, 2, 3, 4, 9, 8, 7, 6, 5, 3]
    console.log("Testing: " + data + " result: " + find_duplicate(data))
}
// test_find_duplicate()

export default find_duplicate

