
function rotateArray(arr, d) {
    const n = arr.length;
    d %= n;
    return [...arr.slice(d), ...arr.slice(0, d)];
}

const arr = [1, 2, 3, 4, 5];
const rotations = parseInt(prompt("Enter number of rotations: "), 10);
console.log("Rotated array:", rotateArray(arr, rotations));
