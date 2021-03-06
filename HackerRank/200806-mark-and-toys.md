# [Mark and Toys](https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting)

> Easy

<br />

## 문제 이해

가지고 있는 금액 안에서 최대한 많은 갯수의 장난감을 사려고 한다.
`장난감 가격 리스트(배열)`과 `소지 금액`을 인자로 받아서 살 수 있는 장난감의 최대 갯수를 리턴하면 된다.

<br />

## 코드 구현 & 풀이 학습

```js
function swap(arr, i, j) {
  const tmp = arr[i];
  arr[i] = arr[j];
  arr[j] = tmp;
}

function maximumToys(prices, k) {
  const len = prices.length;
  let sum = 0;
  let minIdx;

  for (let i = 0; i < len; i++) {
    minIdx = i;
    for (let j = i + 1; j < len; j++) {
      if (prices[minIdx] > prices[j]) minIdx = j;
    }
    const tmp = sum + prices[minIdx];
    if (tmp > k) return i;
    if (tmp === k) return i + 1;
    if (i !== minIdx) swap(prices, i, minIdx);
    sum = tmp;
  }

  return len;
}

// 시간복잡도 : O(n^2)
// 공간복잡도 : O(1)
```

모든 가격을 정렬하지 않고도 소지금액으로 살 수 있는 장난감의 갯수를 즉시 반환하고 싶어서 선택정렬을 사용하기로 했다.  
선택정렬을 사용하면 왼쪽부터 차례대로 오름차순 정렬을 하기 때문이다.

정렬과 동시에 정렬된 가격들의 합(`sum`)을 업데이트 하다가 `sum`이 소지금액인 `k`보다 작거나 같을 경우 구매 가능한 장난감의 갯수를 즉시 리턴하도록 했다.  
(장난감의 갯수는 `prices`의 인덱스로 알 수 있다.)

엄밀히 말하면 `sum`을 `k`와 직접 비교하지는 않고, `sum + prices[min]`을 `k`와 비교한다. 불필요하게 swap을 하지 않기 위해서이다.

- `sum + prices[min] > k` 인 경우 즉시 아이템의 갯수 `i`를 리턴하고 (-> swap할 필요가 없음)
- `sum + prices[min] === k` 인 경우 아이템의 갯수 `i + 1`를 리턴하고 (-> swap할 필요가 없음)
- `sum + prices[min] < k` 인 경우에는 **`i`가 `minIdx`와 다를 경우에만 swap**을 시켜준 뒤 `sum`을 `sum + prices[min]`로 대체한다. (즉, `sum`에 새로운 최소값을 더해서 업데이트 시켜준다.)
