export function minMax(given: number[]): number[] {
    let min: number = given[0];
    let max: number = given[0];

    for (let n of given) {
        if (n<min) {
            min = n;
        }
        if (n>max) {
            max = n;
        }
    }

    return [min, max];
}

export function minMaxGolf(given: number[]): number[] {
    return [Math.min(...given), Math.max(...given)]
}