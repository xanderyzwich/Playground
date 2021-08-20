export function toList(o: {[key: string]: number}): Array<Array<string|number>>{
    let result = new Array<Array<string|number>>()
    for (let key of Object.keys(o)) {
        result.push([key, o[key]])
    }
    return result
}
export function toListMap(o: {[key: string]: number}): Array<Array<string|number>>{
    let result = new Array<Array<string|number>>()
    Object.keys(o).map(function (val, index){
        result.push([val, o[val]])
    })
    return result
}