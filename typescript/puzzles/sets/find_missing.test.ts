import { find_missing } from ".././sets/find_missing";

describe("Testing find_missing", () => {
    test("Does it work?", () => {
        let data = [5, 4, 3, 1, 6, 7, 8, 9];
        expect(find_missing(data)).toBe(2);
    })
})