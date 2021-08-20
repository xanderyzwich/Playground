import { toListMap as toList} from "./object_list_convertion"

describe("Does it work?", () => {
    test("test one", () => {
        expect(toList({ a: 1, b: 2 })).toStrictEqual([["a", 1], ["b", 2]])
    }),
    test("test two", () => {
        expect(toList({ shrimp: 15, tots: 12 })).toStrictEqual([["shrimp", 15], ["tots", 12]])
    }),
    test("test three", () => {
        expect(toList({})).toStrictEqual([])
    })
})