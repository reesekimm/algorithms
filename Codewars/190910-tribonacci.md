### 6kyu / Javascript

# [Tribonacci Sequence](https://www.codewars.com/kata/tribonacci-sequence/train/javascript)

## 문제

Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

If you enjoyed this kata more advanced and generalized version of it can be found in the Xbonacci kata

<br />

#### Example

```
tribonacci([1,1,1],10),[1,1,1,3,5,9,17,31,57,105]
tribonacci([0,0,0],10),[0,0,0,0,0,0,0,0,0,0]
tribonacci([1,1,1],1),[1]
tribonacci([300,200,100],0),[]
```

<br />

## 문제 이해

피보나치 수열이 숫자를 2개씩 더해서 나열했다면, 트리보나치는 숫자를 3개씩 더해서 나열한 것이다.  
함수 tribonacci는 수열의 맨 앞에 오는 숫자 3개를 담은 배열 `signature`와 0보다 크거나 같은 정수 `n`을 인자로 받는다. 그리고 n번째까지의 트리보나치 수열을 계산해서 배열의 형태로 리턴해준다. (n이 0일 경우 빈 배열을 리턴)

<br />

## 코드 구현

```javascript
function tribonacci(signature, n) {
  if (!n) return [];
  if (n <= 3) return [signature[n - 1]];

  let result = [].concat(signature); // signature 원본 보호
  for (let i = 3; i < n; i++) {
    result.push(result[i - 3] + result[i - 2] + result[i - 1]);
  }
  return result;
}
```

<br />

## 다른 솔루션 분석

### 1.

```javascript
function tribonacci(signature, n) {
  const result = signature.slice(0, n);
  while (result.length < n) {
    result[result.length] = result.slice(-3).reduce((p, c) => p + c, 0);
  }
  return result;
}
```

- 변수 result의 초기값으로 `signature.slice(0, n)`을 할당하면서 내가 if문을 사용해서 선처리해줬던 요건들을 한 줄로 정리했다.  
  (n이 0일 경우 result는 빈 배열이 되고, n이 signature의 길이보다 작을 경우 필요한 부분까지만 복사해주기 때문)
- n이 4 이상일 경우에만 while문을 돌게 되는데, 이때 **`result.length`를 인덱스로 활용**해서 배열 result의 길이를 점점 늘려나간다.
- tribonacci 계산을 위해서 `slice(-3).reduce((p, c) => p + c, 0)`를 쓴 점도 인상깊다.

<br />

### 2.

```javascript
function tribonacci(s, n) {
  var arr = [];
  for (var i = 0; i < n; i++) {
    arr.push(i < 3 ? s[i] : arr[i - 1] + arr[i - 2] + arr[i - 3]);
  }
  return arr;
}
```

- n이 0인 경우 for문의 조건에 부합하지 않기 때문에 그대로 빈 배열을 리턴한다.
- n이 0이 아닌 경우엔 for문에 진입하고, push의 인자 위치에 들어있는 조건문에 따라 n번째 까지의 트리보나치 수를 arr에 넣어준다.
