# [Bubble Sort](https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting)

> Easy

<br />

## 문제 이해

bubble sort 구현

<br />

## 코드 구현 & 풀이 학습

```js
function swap(arr, i, j) {
  const tmp = arr[i];
  arr[i] = arr[j];
  arr[j] = tmp;
}

function countSwaps(a) {
  const len = a.length;

  let swaps = 0;
  for (let i = 0; i < len; i++) {
    for (let j = 0; j <= i; j++) {
      if (a[j] > a[i]) {
        swap(a, i, j);
        swaps++;
      }
    }
  }

  console.log(
    `Array is sorted in ${swaps} swaps.\nFirst Element: ${a[0]}\nLast Element: ${a[len - 1]}`
  );
}

// 시간복잡도 : O(n^2)
// 공간복잡도 : O(1)
```
