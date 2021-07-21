import { generate } from "./generate";

describe("Testing generate", () => {
    test("Does it work?", () => {
        expect(generate(10)).toStrictEqual([1,2,3,4,5,6,7,8,9,10]);
    })
})