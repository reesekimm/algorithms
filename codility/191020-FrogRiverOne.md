Lesson 04 - Counting Elements | [FrogRiverOne](https://app.codility.com/programmers/lessons/4-counting_elements/)

## 문제

A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. `A[K]` represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

```
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
```

In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

```
function solution(X, A);
```

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

```
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
```

the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

- N and X are integers within the range `[1..100,000]`;
- each element of array A is an integer within the range `[1..X]`.

<br />

## 문제 이해

개구리가 초기 위치 `0` 에서 너비가 `X`인 강을 건너 `X + 1`로 이동하려고 한다. 강을 건널 때는 강 위로 떨어진 나뭇잎 위를 밟고 지나가야 하는데, 나뭇잎의 위치정보가 배열로 제공된다. 배열의 인덱스는 나뭇잎이 떨어진 시간을 나타내고 각각의 값은 나뭇잎이 떨어진 위치를 나타낸다.

만약 강의 너비 X가 5이고 나뭇잎의 위치정보가 담긴 배열 A가 다음과 같다면,

```
  A[0] = 1  // 나뭇잎이 0초에 위치 1에 떨어졌다.
  A[1] = 3  // 나뭇잎이 1초에 위치 2에 떨어졌다.
  A[2] = 1  // 나뭇잎이 2초에 위치 3에 떨어졌다.
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
```

나뭇잎은 강물에 떠내려가지 않고 떨어진 위치에 고정되어 있다고 가정한다. 따라서 6초가 되면 1부터 5까지 모든 길목에 나뭇잎이 위치하면서 강을 건널 수 있다.<br />
→ 강을 건너는데 필요한 최소 시간은 6초라고 할 수 있다.

우리는 강의 너비를 뜻하는 `정수 X`와 나뭇잎의 위치정보를 담은 `배열 A`를 인자로 받아서 `강을 건널 수 있는 최단시간`을 구하면 된다.

<br />

## 문제 풀이 & 코드 구현

```js
function solution(X, A) {
  let container = Array(X).fill(null);
  for (let i = 0; i < A.length; i++) {
    container[A[i] - 1] = A[i];
    if (container.includes(null)) {
      continue;
    } else {
      return i;
    }
  }
  return -1;
}
```

길이가 X인 임의의 배열을 만들고 모든 값을 null로 채운 후 배열 A에 loop을 돌면서 null을 숫자로 치환해나갔다. 임의의 배열이 전부 숫자로 채워지면 1부터 X까지 모든 숫자가 등장했다는 의미이기 때문에 X가 담긴 인덱스를 리턴하고, 그렇지 않을 경우 A의 마지막 요소까지 loop을 돌아서 최종적으로 -1을 리턴한다.

코드 수행 결과 시간복잡도 O(n)에 정확도는 100% 충족했지만 성능에서 timeout 에러가 발생했다.

<img src="https://user-images.githubusercontent.com/42695954/67159743-f1880780-f383-11e9-9652-bad05df440b5.PNG" width="500" />

<br />

## Solution

```js
function solution(X, A) {
  let holdValues = new Set();
  for (i = 0; i < A.length; i++) {
    holdValues.add(A[i]);
    if (holdValues.size === X) {
      return i;
    }
  }
  return -1;
}
```

- 중복되는 값을 무시하는 set의 성질을 이용해서 1부터 X까지 각각의 값이 중복없이 존재하도록 하고, set의 `size`속성을 사용해서 loop를 돌지 않고 즉시 인덱스를 리턴했다.
