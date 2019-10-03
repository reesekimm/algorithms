Lesson 02 - Arrays | [CyclicRotation](https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/)

## 문제

An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

```
function solution(A, K);
```

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3

the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

For another example, given

    A = [0, 0, 0]
    K = 1

the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4

the function should return [1, 2, 3, 4]

Assume that:

- N and K are integers within the range `[0..100]`;
  each element of array A is an integer within the range `[−1,000..1,000]`.
- In your solution, focus on **correctness**. The performance of your solution will not be the focus of the assessment.

<br />

## 문제 이해

N개의 숫자가 담긴 배열`A`와 정수`K`를 인자로 받아서 배열의 숫자들을 오른쪽으로 K번 이동시킨 배열을 리턴한다.

```
A = [3, 8, 9, 7, 6], K = 3 일 경우
[9, 7, 6, 3, 8]을 리턴.
```

> 성능이 아닌 정확성에 초점을 맞춘다.

<br />

## 풀이 과정

요소를 배열의 길이 만큼 오른쪽으로 이동했을 경우 다시 원래 위치로 돌아온다는 점을 이용해서 K번 이동 후 최종 위치(인덱스)가 어딘지 계산한 후 요소들을 새로운 배열에 재배치시켰다.

<br />

## 코드 구현

```js
function solution(A, K) {
  let result = [];
  let length = A.length;

  A.forEach((num, i) => {
    let newIdx = (i + K) % length;
    result[newIdx] = num;
  });

  return result;
}
```

![2019-10-03 14;27;41](https://user-images.githubusercontent.com/42695954/66101747-e6df1b80-e5ea-11e9-9183-b30535c736fd.PNG)

<br />

## 다른 방법으로 풀어보기

```js
function solution(A, K) {
  let length = A.length;
  if (K === length) return A;

  let gap = K % length;
  let front = A.slice(length - gap);
  let back = A.slice(0, length - gap);

  return front.concat(back);
}
```

K번 오른쪽으로 이동했을 때 배열의 길이를 넘어서는 요소의 인덱스를 기점으로 배열을 복사해서 분리한 후 `concat`으로 이어붙여서 리턴해주었다.

이런 접근방식을 택한 이유는 `forEach`로 배열을 순회하지 않고 시간복잡도를 개선하기 위해서 였는데 풀고나서 찾아보니 `slice`의 big-O가 O(1)이 아닌 [O(n)](https://stackoverflow.com/questions/22614237/javascript-runtime-complexity-of-array-functions)이었다. 이렇게되면 경우에따라 첫번째 풀이보다 성능이 떨어진다;

slice의 big-O가 O(n)이라는 걸 기억해두자:)
