import { remove_duplicates } from "./remove_duplicates";

describe("Test remove_duplicates", () => {
    test("Compare with bubble_sort", () =>{
        let data = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 7, 9];
        expect(remove_duplicates(data)).toStrictEqual([1, 2, 3, 4, 5, 6, 7, 8, 9]);
    })
})