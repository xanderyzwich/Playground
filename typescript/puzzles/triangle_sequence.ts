export function triangleStandard(rows: number): number {
    let accumulator: number = 0;
    for (let i = 1; i<=rows; i++) {
        accumulator += i;
    }
    return accumulator
}

export function triangleRecursive(rows: number): number {
    if (rows === 1) {
        return 1
    }
    else {
        return rows + triangleRecursive(rows-1)
    }
}

export function triangleMath(rows: number): number {
    return rows * (rows+1) / 2
}