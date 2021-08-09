import { minMaxGolf as minMax } from "../../../puzzles/sets/min_max"

describe("Testing the minMax function", ()  => {
    test("One through five", () => {
        expect(minMax([1,2,3,4,5])).toStrictEqual([1, 5]);
    }),
    test("Two items", () => {
        expect(minMax([2334454, 5])).toStrictEqual([5, 2334454]);
    }),
    test("One item", () => {
        expect(minMax([1])).toStrictEqual([1, 1]);
    })
})