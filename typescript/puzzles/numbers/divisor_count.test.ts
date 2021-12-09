import { divisors } from "./divisor_count"

describe("Does it work?", () => {
    test("test four", () => {
        expect(divisors(4)).toEqual(3)
    }),
    test("test five", () => {
        expect(divisors(5)).toEqual(2)
    }),
    test("test twelve", () => {
        expect(divisors(12)).toEqual(6)
    }),
    test("test thirty", () => {
        expect(divisors(30)).toEqual(8)
    })    
})