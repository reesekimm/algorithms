# [Alternating Characters](https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings)

> Easy

<br />

## 문제 이해

문자열을 인자로 받아서 같은 문자가 연속으로 등장하지 않도록 '지워야 하는 문자의 개수'를 구하는 문제

<br />

## 코드 구현 & 풀이 학습

```js
function alternatingCharacters(s) {
  return s.split("").reduce((deletions, char, i, arr) => {
    if (char === arr[i - 1]) deletions++; // O(1)
    return deletions;
  }, 0);
  // O(n)
}
```

인자로 받은 문자열을 배열로 강제변환한 뒤 reduce를 사용하여 모든 요소를 순회하면서 인접한 문자(`arr[i]`)와 현재 처리하고 있는 문자(`char`)를 비교하고, 두 값이 같을 경우 지워야 하는 문자의 갯수(`deletions`)를 1 더해주었다.  
reduce 메소드는 배열의 모든 요소에 대해 reducer를 실행하기 때문에 O(n)의 시간복잡도를 가지고, reducer 내부에서 값을 비교하고 업데이트하는 로직은 O(1)의 시간복잡도를 가지기 때문에 전체적인 시간복잡도는 O(n) 이다.
