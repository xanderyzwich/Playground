import { lastWordLength } from "./last_word_length"

describe("Testing lastWordLength function", () => {
    test("first", () => {
        expect(lastWordLength("Hello World")).toBe(5)
    }),
    test("second", () => {
        expect(lastWordLength("   fly me   to   the moon  ")).toBe(4)
    }),
    test("third", () => {
        expect(lastWordLength("luffy is still joyboy")).toBe(6)
    })
})