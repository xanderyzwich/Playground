import { find_duplicate } from "../../../puzzles/sets/find_duplicate";

describe("Testing find_duplicate", () => {
    test("Does it work?", () => {
        let data : number[] = [1, 2, 3, 4, 9, 8, 7, 6, 5, 3]
        expect(find_duplicate(data)).toBe(3);
    })
})