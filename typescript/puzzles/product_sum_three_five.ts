export function sum_of_multiples(n: number): number {
    let running_sum: number = 0

    for (let i: number = 3; i < n; i+=3) {
        running_sum += i;
    }
    for (let i: number = 5; i < n; i+=5) {
        if (i%3 != 0) {
            running_sum += i;
    }}
    return running_sum;
}