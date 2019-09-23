Lesson 01 - Iterations | [Binary Gap](https://app.codility.com/programmers/lessons/1-iterations/binary_gap/)

## Test Description

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

```
function solution(N);
```

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

- N is an integer within the range 1 ~ 2,147,483,647.

<br />

## 문제 이해

1부터 2,147,483,647 까지의 양의 정수를 인자로 받아서 2진수로 변환했을 때 **1로 둘러쌓인 연속된 0의 최대 갯수**를 구하는 문제이다.

```
N = 32 = 100000 → 0
N = 1162 = 10010001010 → 3
N = 805306373 = 110000000000000000000000000101 → 25
```

<br />

## 풀이 과정

1. 정수를 이진수 문자열로 변환한다. (loop를 돌기 위함)
2. 변수 `max`(=0의 최대 갯수)와 `count`(=0의 갯수)를 만든다.
3. 이진수 문자열에 loop를 돌면서 0의 갯수를 세서 `count`를 업데이트 해주고 `count`를 `max`를 비교하여 `max`값을 업데이트 한다.
4. 최종적으로 `max`를 리턴해준다.

<br />

## 코드 구현

```js
function solution(N) {
  let binary = N.toString(2);
  let length = binary.length;
  let max = 0;
  let count = 0;

  for (let i = 0; i < length; i++) {
    if (binary[i] === "0") {
      if (i === length - 1) {
        return max;
      }
      count++;
    } else {
      if (max < count) {
        max = count;
      }
      count = 0;
      continue;
    }
  }
  return max;
}
```

<br />

## 코드 분석

Big-O

```js
function solution(N) {
  let binary = N.toString(2); // O(1)
  let length = binary.length;
  let max = 0;
  let count = 0;

  for (let i = 0; i < length; i++) {
    // O(n)
    if (binary[i] === "0") {
      if (i === length - 1) {
        return max;
      }
      count++;
    } else {
      if (max < count) {
        max = count;
      }
      count = 0;
      continue;
    }
  }
  return max;
}
```

**O(n)**의 시간복잡도를 가진다.

<br />

## 다른 방법으로 풀어보기

### 1.

```js
function solution(N) {
  let tmp = [];
  while (N > 0) {
    // O(log n)
    tmp.push(N % 2);
    N = Math.trunc(N / 2);
  }

  let binary = tmp.reverse(); // O(1)
  let count = 0;
  let max = 0;

  for (let i = 0; i < binary.length; i++) {
    // O(n)
    if (binary[i] === 0) {
      if (i === binary.length - 1) {
        return max;
      }
      count++;
    } else {
      max = Math.max(max, count);
      count = 0;
    }
  }
  return max;
}
```

- 10진수를 2진수로 변환할 때 `toString(2)`을 쓰지 않고 직접 계산
  > ```
  > 18 / 2 = 9, 나머지는 0
  > 9 / 2 = 4, 나머지는 1
  > 4 / 2 = 2, 나머지는 0
  > 2 / 2 = 1, 나머지는 0
  > 1 / 2 = 0, 나머지는 1
  > ```
  >
  > ```
  > 18(10) = 1 * 16 + 0 * 8 + 0 * 4 + 1 * 2 + 0 * 1 = 10010(2)
  > ```
- 주어진 값의 소수부분을 제거하고 정수부분만 반환하기 위해 `Math.trunc()`사용
- 최대값을 구할 때 if문이 대신 `Math.max()` 사용
- 최종적인 시간복잡도는 O(n)

<br />

### 2.

```js
function solution(N) {
  let binary = N.toString(2); // O(1)

  let one = [];
  for (let i = 0; i < binary.length; i++) {
    // O(n)
    if (binary[i] === "1") {
      one.push(i);
    } else {
      continue;
    }
  }

  let gap = [];
  for (let i = 1; i < one.length; i++) {
    // O(n)
    gap.push(one[i] - one[i - 1] - 1);
  }

  return gap.reduce((max, num) => (max < num ? (max = num) : (max = max)), 0); // O(n)
}
```

- 2진수에서 1이 등장할 때 마다 인덱스값을 배열 `one`에 넣기
- 배열A에서 인접한 요소끼리 뺄셈을 해서 연속된 0의 갯수를 구해 배열B에 넣기
- 배열B에서 최대값을 최종 결과값으로 리턴
- 최종적인 시간복잡도는 O(n)

<br />

---

**다른 풀이 참조**

- [JavaScript Tech Interview Exercise 2: Binary Gap Exercise in Codility](http://www.zsoltnagy.eu/javascript-tech-interview-exercise-2-binary-gap-exercise-in-codility/)
- [codility - BinaryGap (시간복잡도 평가 추가)](https://wayhome25.github.io/algorithm/2017/04/24/binarygap/)
