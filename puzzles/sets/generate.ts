
function generate(count:number) : number[] {
    var output_arr : number[] = new Array(count)
    for (var i = 1; i <= count; i++) {
        output_arr[i-1] = i
    }
    return output_arr
}
function test_generate() {
    let data : number[] = generate(10)
    console.log(data)
}

export default generate