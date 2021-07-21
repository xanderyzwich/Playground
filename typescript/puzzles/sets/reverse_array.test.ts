import { reverse_array } from "./reverse_array"

describe("Testing reverse array", () => {
    test("title", () => {
        let data = [1, 2, 3, 4, 5, 6, 7, 8, 9];
        reverse_array(data);
        expect(data).toStrictEqual([9, 8, 7, 6, 5, 4, 3, 2, 1]);
    })
})