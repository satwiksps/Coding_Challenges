
function selectionSort(arr, n = arr.length, index = 0) {
    if (index == n) return arr;

    let minIndex = index;
    for (let i = index + 1; i < n; i++) {
        if (arr[i] < arr[minIndex]) {
            minIndex = i;
        }
    }
    [arr[index], arr[minIndex]] = [arr[minIndex], arr[index]];

    return selectionSort(arr, n, index + 1);
}

const arr = [29, 10, 14, 37, 13];
console.log("Sorted array:", selectionSort(arr));
