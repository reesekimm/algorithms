Lesson 03 - Time Complexity | [TapeEquilibrium](https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/)

## 문제

A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: `A[0], A[1], ..., A[P − 1]` and `A[P], A[P + 1], ..., A[N − 1]`.

The difference between the two parts is the value of: `|(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|`

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

```
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
```

We can split this tape in four places:

```
P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
```

Write a function:

```
function solution(A);
```

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

```
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
```

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

- N is an integer within the range `[2..100,000]`;
- each element of array A is an integer within the range `[−1,000..1,000]`.

<br />

## 문제 이해

배열 A는 N개의 정수로 구성된 배열이다. 이때 임의의 인덱스 P를 기준으로 '`A[0]`부터 `A[P-1]`까지 모든 숫자들의 합' 에서 `A[P]`부터 `A[N-1]`까지 모든 숫자의 합을 빼서 그`차이`의 **절대값**을 구한다.<br />

차이 = `|(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|`

당연히 `P`가 달라지면 `차이`가 달라지게 되는데, 우리는 **`차이`가 가질 수 있는 가장 작은 값을 리턴**해주는 함수를 작성하면 된다.

<br />

## 문제 풀이 & 코드 구현

### 1차

```js
function solution(A) {
  let first, second;
  let diffs = [];

  for (let p = 1; p < A.length; p++) {
    first = 0;
    second = 0;
    for (let i = 0; i < p; i++) {
      first += A[i];
    }
    for (let j = p; j < A.length; j++) {
      second += A[j];
    }
    diffs.push(Math.abs(first - second));
  }

  return Math.min(...diffs);
}
```

혹시나 해서 문제의 내용을 그대로 코드로 옮겼다. `P`가 변할때마다 루프를 돌며 first 파트와 second 파트의 합을 계산한다. 역시 배열의 크기가 커지면 Timeout 에러가 발생했다.

<img src="https://user-images.githubusercontent.com/42695954/66760208-974afa80-eedc-11e9-9c88-a85fb63195c9.PNG" width="500" />

<br />

### 2차

```js
function solution(A) {
  let total = A.reduce((sum, num) => (sum += num), 0);
  let first = A[0];
  let second = total - first;
  let diff = Math.abs(first - second);

  for (let p = 2; p < A.length; p++) {
    first += A[p - 1];
    second = total - first;
    let newDiff = Math.abs(first - second);
    if (diff > newDiff) {
      diff = newDiff;
    }
  }
  return diff;
}
```

- 배열에 들어있는 모든 숫자의 합(`total`)을 구한 후 first 파트(`first`), second 파트(`second`), 그리고 그 차이(`diff`)를 차례대로 계산해서 초기값으로 할당했다.

- `P`가 1씩 커질 때마다 `first`, `second`, `diff`를 갱신하면서 `diff`가 최소값을 가지도록 하는데, 이때 루프를 돌지 않고 각각의 값들이 가지는 관계를 토대로 덧셈/뺄셈을 사용했다.

- 결과적으로 배열의 크기가 커져도 효과적으로 처리할 수 있게 되었다.

![right answer](https://user-images.githubusercontent.com/42695954/66761885-ddee2400-eedf-11e9-9bd6-359875166ddb.PNG)
