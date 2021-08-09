import { ipsbetween } from "./ipv4_difference";

describe("Testing IPV4 count between given IP addresses", () => {
    test("'10.0.0.0', and '10.0.0.50'", () =>{
        expect(ipsbetween("10.0.0.0", "10.0.0.50")).toBe(50);
    });
    test("'10.0.0.0', and '10.0.1.0'", () =>{
        expect(ipsbetween("10.0.0.0", "10.0.1.0")).toBe(256);
    });
    test("'20.0.0.10', and '20.0.1.0'", () =>{
        expect(ipsbetween("20.0.0.10", "20.0.1.0")).toBe(246);
    });
    test("'20.0.0.10', and '20.1.1.0'", () =>{
        expect(ipsbetween("20.0.0.10", "20.1.1.0")).toBe(65782);
    });
})