Lesson 02 - Arrays | [OddOccurrencesInArray](https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/)

## 문제

A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

```
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
```

the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

```
function solution(A);
```

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

```
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
```

the function should return 7, as explained in the example above.

Write an **efficient** algorithm for the following assumptions:

- N is an odd integer within the range 1 to 1,000,000;
- each element of array A is an integer within the range 1 to 1,000,000,000;
- all but one of the values in A occur an even number of times.

<br />

## 문제 이해

N개의 숫자를 담은 배열을 인자로 받아서 홀수 번 등장하는 숫자를 리턴해준다.

<br />

## 풀이 과정

맨 처음에는 문제를 제대로 안 읽어서 짝이 없는 1개의 숫자를 구하는 것으로 잘못 접근했다. (즉, 다른 모든 숫자는 짝수개씩 존재하지만 한 숫자는 1개밖에 없는 것으로 이해..) 이때 풀이 방식은 다음과 같았다.

1. 배열을 정렬한다.
2. 각 숫자가 등장하는 첫번째 인덱스와 마지막 인덱스를 구해서 두 인덱스가 같으면 해당 숫자를 리턴한다.

<br />

## 코드 구현 (1차)

```js
function solution(A) {
  let ordered = A.sort();

  let i = 0;
  let length = ordered.length;

  while (i < length) {
    let first = ordered.indexOf(ordered[i]);
    let last = ordered.lastIndexOf(ordered[i]);
    if (first === last) {
      return ordered[i];
    } else {
      i = last + 1;
    }
  }
}
```

![2019-09-24 14;42;54](https://user-images.githubusercontent.com/42695954/65484184-9b858880-ded9-11e9-8390-e6310dc5c7d0.PNG)

당연히 정확도 및 성능 측면에서 좋은 평가를 받지 못했다.
시간복잡도는 `O(n**2)`로 최악이었다. while문 안에 있는 `indexOf`와 `lastIndexOf`의 영향이 컸다.

전달받은 인자를 콘솔에 출력해서 핸들링 하지 못한 케이스가 있는지 찾아보기도 하고 고 좀 더 효율적이라고 생각되는 코드를 작성해보기도 했지만 평가점수가 나아지지는 않았다. 한참 헤매다가 문제를 다시 읽고 한 번이 아닌 홀수 번 등장하는 숫자를 찾아야 한다는걸 알았다;;

<br />

## 코드구현 (2차)

```js
function solution(A) {
  let count = {};
  A.forEach(num => (count[num] = (count[num] || 0) + 1));

  for (let prop in count) {
    if (count[prop] % 2) {
      return +prop;
    }
  }
}
```

![2019-09-24 14;55;54](https://user-images.githubusercontent.com/42695954/65484969-70039d80-dedb-11e9-9e72-472fa7688840.PNG)

통과!  
시간복잡도는 `O(n)` 또는 `O(N*log(N))`으로 측정됐다.

<br />

## 다른 풀이 방법

```js
function solution(A) {
  var result = 0;
  for (var i = 0; i < A.length; i++) {
    result ^= A[i];
  }
  return result;
}
```

비트 XOR 연산자를 사용한 풀이다. XOR 연산자는 대응되는 두 비트가 서로 다르면 1을 반환하고, 서로 같으면 0을 반환한다.  
`result`와 `A[i]`가 같으면 `0`, 다르면 `0`이 아닌 값으로 `result`를 업데이트 해나간다. loop가 종료되면 최종적인 `result`는 홀수번 등장하는 값이 된다.

- [참고1](http://tcpschool.com/javascript/js_operator_bitwise)
- [참고2](http://blog.naver.com/PostView.nhn?blogId=mouse226&logNo=221304567474&parentCategoryNo=&categoryNo=62&viewDate=&isShowPopularPosts=true&from=search)

<br />

## 기타 느낀점

- 문제를 잘 읽자. 오늘처럼 엉뚱하게 접근해서 삽질하지 말고~!
- 비트 연산자를 잘 쓰면 코드가 획기적으로 짧아지는 것 같다.
