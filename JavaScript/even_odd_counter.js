function countEvenOdd(arr) {
    let even = 0, odd = 0;
    for (let num of arr) {
        if (num % 2 === 0) even++;
        else odd++;
    }
    return { even, odd };
}
console.log(countEvenOdd([1, 2, 3, 4, 5, 6]));
