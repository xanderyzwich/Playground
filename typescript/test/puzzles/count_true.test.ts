import { countTrue } from "../../puzzles/count_true"


describe("Does it work?", () =>{
    test("Test Case 1", () =>{
        expect(countTrue([true, false, false, true, false])).toBe(2);
    }),
    test("Test Case 2", () => {
        expect(countTrue([false, false, false, false])).toBe(0);
    }),
    test("Test Case 3", () => {
        expect(countTrue([])).toBe(0);
    })
})