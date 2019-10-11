Lesson 03 - Time Complexity | [PermMissingElem](https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/)

## 문제

An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

```
function solution(A);
```

that, given an array A, returns the value of the missing element.

For example, given array A such that:

```
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
```

the function should return 4, as it is the missing element.

Write an **efficient** algorithm for the following assumptions:

- N is an integer within the range [0..100,000];
- the elements of A are all distinct;
- each element of array A is an integer within the range [1..(N + 1)].
  <br />

## 문제 이해

A는 길이가 N인 배열이고 1부터 N + 1까지의 서로 다른 정수로 구성되어 있다. 이러한 조건 때문에 숫자 한 개는 A에 포함되지 않게 된다.

예를들어 배열 A가 [2, 3, 1, 5] 라면 누락된 숫자는 4이다.

아래의 조건 3가지를 고려해서 누락된 숫자를 찾는 함수를 작성하면 된다.

1. N의 범위 : 0 ~ 100,000
2. A는 각기 다른 숫자로 구성되어 있다.
3. A에 들어있는 숫자들의 범위 : 1 ~ N + 1

<br />

## 문제 풀이 & 코드 구현

### 1차

```js
function solution(A) {
  let comparisonArr = [...Array(A.length + 1).keys()].map(el => (el += 1));
  for (let i = 0; i < comparisonArr.length; i++) {
    if (A.indexOf(comparisonArr[i]) === -1) {
      return comparisonArr[i];
    }
  }
}
```

![2019-10-11 11;38;08](https://user-images.githubusercontent.com/42695954/66620523-c5e67e00-ec1b-11e9-8d10-8eeb8d947d46.PNG)

1부터 N + 1 까지의 숫자를 담은 배열을 생성하여 A와 비교하고 특정 숫자가 A에 없을 경우 해당 숫자를 리턴하는 가장 단순한 접근 방식으로 풀어봤다. 시간복잡도는 `O(n**2)`이 나오고 A의 크기가 최대치로 커지면 timeout 에러가 발생했다.

<br />

### 2차

```js
function solution(A) {
  A.sort((a, b) => a - b);
  for (let i = 0; i <= A.length; i++) {
    if (A[i] === i + 1) {
      continue;
    } else {
      return i + 1;
    }
  }
}
```

![2019-10-11 11;18;53](https://user-images.githubusercontent.com/42695954/66620087-3391aa80-ec1a-11e9-93a9-d513656e0373.PNG)

A를 오름차순을 정렬하고 순회하면서 인덱스와 비교하여 누락된 숫자를 찾았다. A가 빈배열이거나 누락된 숫자가 N + 1인 경우를 핸들링해주려면 반드시 인덱스가 `A.length`와 같은 경우도 고려해주어야 한다. 시간복잡도는 `O(N)` or `O(N * log(N))`이 나왔다.
