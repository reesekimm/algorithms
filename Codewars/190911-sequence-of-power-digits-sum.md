### 5kyu / Javascript

# [Sequence of Power Digits Sum](https://www.codewars.com/kata/sequence-of-power-digits-sum/javascript)

## 문제

Let's take an integer number, start and let's do the iterative process described below:

- we take its digits and raise each of them to a certain power, n, and add all those values up. (result = r1)
- we repeat the same process with the value r1 and so on, k times.

Let's do it with `start = 420, n = 3, k = 5`

```
420 ---> 72 (= 4³ + 2³ + 0³) ---> 351 (= 7³ + 2³) ---> 153 ---> 153 ----> 153
```

We can observe that it took 3 steps to reach a cyclical pattern [153](h = 3). The length of this cyclical pattern is 1, patt_len. The last term of our k operations is 153, last_term

Now, `start = 420, n = 4, k = 30`

```
420 ---> 272 ---> 2433 ---> 434 ---> 593 ---> 7267 --->
6114 ---> 1554 ---> 1507 ---> 3027 ---> 2498 ---> 10929 --->
13139 ---> 6725 ---> 4338 ---> 4514 ---> 1138 ---> 4179 ---> 9219 --->
13139 ---> 6725 ---> 4338 ---> 4514 ---> 1138 ---> 4179 ---> 9219 --->
13139 ---> 6725 ---> 4338 ---> 4514 ---> 1138 ---> 4179 ---> 9219......
```

In this example we can observe that the cyclical pattern (`cyc_patt_arr`) is `[13139, 6725, 4338, 4514, 1138, 4179, 9219]` with a length of `7`, (`patt_len = 7`), and it took `12` steps (`h = 12`) to reach the cyclical pattern. The last term after doing `30` operations is `1138`

Make the function `sum_pow_dig_seq()`, that receives the arguments in the order shown below with the corresponding output:

```
sum_pow_dig_seq(start, n, k) ---> [h, cyc_patt_arr, patt_len, last_term]
```

For our given examples,

```
sum_pow_dig_seq(420, 3, 5) == [3, [153], 1, 153]
sum_pow_dig_seq(420, 4, 30) == [12, [13139, 6725, 4338, 4514, 1138, 4179, 9219], 7, 1138]
```

Constraints for tests:

```
500 ≤ start ≤ 8000
2 ≤ n ≤ 9
100 * n ≤ k ≤ 200 * n
```

Do your best!

<br />

## 문제 이해

작성할 함수 `sum_pow_dig_seq()`는 `start`, `n`, `k` 라는 정수 3개를 인자로 받는다.  
그리고 첫번째 인자인 `start`의 각 자릿수를 `n`제곱하여 더해주는 과정을 반복한다.

sum_pow_dig_seq(420, 3, 5) :

```
420 ---> 72 (= 4³ + 2³ + 0³) ---> 351 (= 7³ + 2³) ---> 153 ---> 153 ----> 153
```

sum_pow_dig_seq(420, 4, 30) :

```
420 ---> 272 ---> 2433 ---> 434 ---> 593 ---> 7267 --->
6114 ---> 1554 ---> 1507 ---> 3027 ---> 2498 ---> 10929 --->
13139 ---> 6725 ---> 4338 ---> 4514 ---> 1138 ---> 4179 ---> 9219 --->
13139 ---> 6725 ---> 4338 ---> 4514 ---> 1138 ---> 4179 ---> 9219 --->
13139 ---> 6725 ---> 4338 ---> 4514 ---> 1138 ---> 4179 ---> 9219......
```

이때 반복해서 등장하는 숫자 패턴이 나오게 되는데, 위 예시들에서는 각각 `[153]`, `[13139, 6725, 4338, 4514, 1138, 4179, 9219]`이 패턴이 된다.

최종적으로는 배열 안에 아래의 4가지를 담아서 리턴해주면 된다.

1. 각 자릿수를 `n`제곱하여 더해주는 과정을 몇 번 거쳐야 패턴의 첫번째 숫자가 등장하는지
2. 숫자 패턴을 담은 배열
3. 숫자 패턴의 길이
4. `k`번째 숫자

<br />

## 문제 풀이

1. 제곱해서 더해주는 계산을 반복해서 그 결과값들을 임의의 배열에 담는다. (패턴이 언제 등장하는지 파악하기 위함)
2. 결과값을 배열에 담기 전에 그 값이 이미 배열에 존재하는지 체크해준다.  
   만약 배열안에 동일한 값이 존재할 경우, 배열 안에서 해당 값을 포함한 이후의 숫자들은 패턴이라고 간주할 수 있다.
3. 최초로 중복해서 등장한 값의 인덱스를 구하면 패턴이 등장하는 시점 역시 구할 수 있다.

<br />

## 코드 구현

```javascript
function sumPowDigSeq(start, n, k) {
  var results = [];
  var sum, idx;
  var appear = false;
  var str = start + "";

  while (!appear) {
    sum = str.split("").reduce((sum, num) => sum + Math.pow(+num, n), 0);
    idx = results.findIndex(el => el === sum);
    if (idx === -1) {
      results.push(sum);
      str = sum + "";
    } else {
      appear = true;
    }
  }

  var patt = results.slice(idx);
  var pattLen = patt.length;
  var cal = (k - idx) % pattLen;
  var kth = patt[cal ? cal - 1 : pattLen - 1];

  return [idx + 1, patt, pattLen, kth];
}
```

<br />

## 다른 솔루션 분석

```javascript
function sumPowDigSeq(start, n, k) {
  const step = i =>
    (function unfold(i) {
      return i && (i % 10) ** n + unfold(Math.floor(i / 10));
    })(i);
  const a = [start].concat(
    Array.from({ length: k }, () => (start = step(start)))
  );
  const j = a.findIndex((v, i) => a.indexOf(v) < i);
  const i = a.indexOf(a[j]);
  return [i, a.slice(i, j), j - i, a[k]];
}
```

1. 즉시실행함수 `step()` 호출 시 재귀함수 `unfold()`가 실행되면서 각 자릿수를 제곱계산하여 합계를 구한다. 제곱계산시에는 `Math.pow()`가 아닌 거듭제곱 연산자 `**`를 사용했다.
2. `stpe()`는 `Array.from()`의 두번째 인자에서 호출되는데, 길이가 k이고 모든 값이 undefine인 배열을 대상으로 실행되는 것을 알 수 있다. 결론적으로 변수 `a`는 계산이 완료된 k개의 값들을 담은 배열을 가리키게 된다.
3. `i`와 `j`를 계산해서 패턴 구간을 찾는다. 이부분은 20분가량 들여다봤는데 이해가 잘 안간다. 흠..

<br />

## 추가로 공부한 내용

#### Array.from()

`Array.from()`은 첫번째 인자로 받는 유사 배열 객체(array-like object)나 반복 가능한 객체(iterable object)를 얕게 복사해서 새로운 Array 객체를 만든다. Array contructor method이기 때문에 `[1, 2, 3].slice()`와 같이 쓸 수 없고 항상 `Array.from()`의 형태로 쓴다.

```
Array.from(arrayLike[, mapFn[, thisArg]])
```

> (1) arrayLike :
>
> 1. 유사 배열 객체 (length 속성과 인덱싱된 요소를 가진 객체)
> 2. 순회 가능한 객체 (Map, Set 등객체의 요소를 얻을 수 있는 객체)
>
> (2) mapFn (optional) : 배열의 모든 요소에 대해 호출할 맵핑 함수
>
> (3) thisArg (optional) : mapFn 실행 시 this로 사용할 값

두번째 매개변수인 mapFn를 입력할 경우 배열의 각 요소를 맵핑할 때 사용할 수 있다. 즉, **`Array.from(obj, mapFn, thisArg)`는 중간에 다른 배열을 생성하지 않는다는 점을 제외하면 `Array.from(obj).map(mapFn, thisArg)`와 같다.**

```javascript
Array.from([1, 2, 3], x => x + x); // [2, 4, 6]
Array.from({ length: 5 }, (v, i) => i * i); // [0, 1, 4, 9, 16]
```

두번째 예제와 같이 length를 표기한 객체에 맵핑함수를 실행하게 되면 `v`에 `undefined`가 할당되면서 인덱스만 담은 배열을 얻을 수 있다. 이때 만약 다음과 같이 `i`가 아닌 `v`를 리턴하면 길이가 5이고 모든 값이 `undefined`인 배열을 얻을 수 있다.

```javascript
Array.from({ length: 5 }, (v, i) => v);
// [undefined, undefined, undefined, undefined, undefined]
```
