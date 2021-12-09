export function divisors(n: number) :number {
    let count: number = 2
    for (let i: number = 2; i <= Math.sqrt(n); i++) {
        if (n%i == 0) {
            count += (i === Math.sqrt(n)) ? 1 : 2
        }
    }
    return count
}