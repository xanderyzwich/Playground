import { bubble_sort } from ".././sets/bubble_sort";

describe("Test bubble_sort", () =>  {
    test("Does it work?", () => {
        let data : number[] = [9, 8, 7, 6, 5, 4, 3, 2, 1];
        bubble_sort(data)
        expect(data).toStrictEqual([1, 2, 3, 4, 5, 6, 7, 8, 9]);
    })
})