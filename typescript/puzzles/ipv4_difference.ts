// Implement a function that 
//     receives two IPv4 addresses, and 
//     returns the number of addresses between them 
//     (including the first one, excluding the last one).
// All inputs will be valid IPv4 addresses in the form of strings. 
// The last address will always be greater than the first one.

export function ipsbetween(ip_one: string, ip_two: string): number {
    const ip_vals_one: string[] = ip_one.split('.');
    const ip_vals_two: string[] = ip_two.split('.');

    if (ip_vals_one.length != ip_vals_two.length) {
        return -1;
    }

    var delta: number = 0;
    for (let i: number = 0; i<ip_vals_one.length; i++) {
        delta *= 256;
        delta += parseInt(ip_vals_two[i]) - parseInt(ip_vals_one[i]);
    }
    return delta;

}