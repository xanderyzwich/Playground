import {triangleMath as triangle} from "./triangle_sequence";

describe("Example Tests for Triangle Sequence", () => {
    test("First Five", () => {
        expect(triangle(1)).toBe(1)
        expect(triangle(2)).toBe(3)
        expect(triangle(3)).toBe(6)
        expect(triangle(4)).toBe(10)
        expect(triangle(5)).toBe(15)
    })
    test("One", () => {
        expect(triangle(1)).toBe(1)
    }),
    test("Six", () => {
        expect(triangle(6)).toBe(21)
    }),
    test("Two Hundred Fifteen", () => {
        expect(triangle(215)).toBe(23220)
    })
})