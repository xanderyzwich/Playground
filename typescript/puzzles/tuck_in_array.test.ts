import { tuckIn } from "./tuck_in_array"

describe("Does tuckIn work?", () => {
    test("first", () => {
        expect(tuckIn([1, 10], [2, 3, 4, 5, 6, 7, 8, 9])).toStrictEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    }),
    test("second", () => {
        expect(tuckIn([15,150], [45, 75, 35])).toStrictEqual([15, 45, 75, 35, 150])
    }),
    test("third", () => {
        expect(tuckIn([[1, 2], [5, 6]], [[3, 4]])).toStrictEqual([[1, 2], [3, 4], [5, 6]])
    })
})