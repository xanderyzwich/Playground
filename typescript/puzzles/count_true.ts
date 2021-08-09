// How Much is True?
// Create a function which returns the number of true values there are in an array.

export function countTrue(data: boolean[]): number {
    let count: number = 0;
    data.forEach(piece => count = piece? count+1: count)
    return count;
}