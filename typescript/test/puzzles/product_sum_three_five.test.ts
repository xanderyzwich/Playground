import { sum_of_multiples } from "../../puzzles/product_sum_three_five";

describe("Testing sum_of_multiples", () => {
    test("10 should return 23", () => {
        expect(sum_of_multiples(10)).toBe(23);
    })
    test("20 should return 78", () => {
        expect(sum_of_multiples(20)).toBe(78);
    })
    test("200 should return 9168", () => {
        expect(sum_of_multiples(200)).toBe(9168);
    })
});