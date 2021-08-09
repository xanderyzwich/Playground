

export function checkCoupon(enteredCode: string, correctCode: string, currentDate: string, expirationDate: string): boolean {
    let current = new Date(currentDate);
    let expiration = new Date(expirationDate);

    console.log("Coupon is valid: " + (current<=expiration));
    
    return false;
}

console.log(checkCoupon('123','123','September 5, 2014','October 1, 2014') === true);
console.log(checkCoupon('123a','123','September 5, 2014','October 1, 2014') === false);