### 5kyu / Javascript

# [Weight for weight](https://www.codewars.com/kata/weight-for-weight/javascript)

## 문제

My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

<br />

#### Example:

"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"

When two numbers have the same "weight", let us class them as if they were strings and not numbers: 100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" (9), it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.

<br />

#### Notes

- it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
- Don't modify the input
- For C: The result is freed.

<br />

## 문제 이해

어떤 피트니스 클럽에서 매 달 회원들의 몸무게 리스트를 공개한다고 한다. 몸무게 리스트를 공개한다는것 자체가 무서운 일이지만.. 더 문제인 것은 몸무게를 '오름차순'으로 정렬한다는 것. 당연히 리스트 맨 마지막에 있는 사람은 회원들 중 가장 뚱뚱한 사람으로 유명해질 수 있다.  
그래서 몸무게 리스트의 순서를 변경하기 위한 함수를 작성하게 되는데, 다음과 같은 원리로 리스트 순서를 바꿔주면 된다.

1. 몸무게 리스트는 `"56 65 74 100 99 68 86 180 90"`과 같이 생겼고, 우리가 작성할 함수는 이 리스트를 인자로 받는다. (리스트가 **문자열**임을 명심!)

2. 숫자별로 각 자릿수를 더해준다.  
   `5 + 6 = 11`, `6 + 5 = 11`, `7 + 4 = 11`, ...  
   1번의 리스트에 있던 몸무게들은 이제 이렇게 변하게 된다.  
   `11 11 11 1 18 14 14 9 9`

3. 이제 **2번에서 처리해준 값들을 기준으로** *기존의 리스트를 오름차순으로 정렬*해서 **문자열**로 리턴해준다.  
   결과는 다음과 같다.  
   `"100 180 90 56 65 74 68 86 99"`  
   여기서 `180`이 `90`보다 앞에 오는 이유는 `180`의 `1`이 `90`의 `9`보다 먼저 오기 때문이다.
   즉, 2번에서 처리한 결과값이 동일할 경우(`180` => `9`, `90` => `9`) 숫자가 아닌 **문자열로 취급하여 정렬**해준다.

4. 주의할 점 : 몸무게 리스트의 앞/뒤와 중간에 불필요한 공백이 있을 수 있다.

<br />

## 코드 구현

```javascript
function orderWeight(str) {
  var tmp = [];

  if (!str) return str;

  let arrOfNumstr = str
    .trim()
    .split(" ")
    .filter(char => char.charCodeAt(char) !== 32);

  let arrOfSum = arrOfNumstr.map(numstr =>
    numstr.split("").reduce((a, b) => Number(a) + Number(b), 0)
  );

  for (let i = 0; i < arrOfSum.length; i++) {
    tmp.push([arrOfNumstr[i], arrOfSum[i]]);
  }

  tmp.sort(function(a, b) {
    if (a[1] < b[1]) {
      return -1;
    } else if (a[1] > b[1]) {
      return 1;
    } else {
      return a[0].localeCompare(b[0]);
    }
  });

  return tmp.map(arr => arr[0]).join(" ");
}
```

<br />

## 다른 방법

```javascript
function orderWeight(list) {
  const sum = str => str.split("").reduce((sum, el) => sum + +el, 0);
  function comp(a, b) {
    let sumA = sum(a);
    let sumB = sum(b);
    return sumA === sumB ? a.localeCompare(b) : sumA - sumB;
  }
  return list
    .split(" ")
    .sort(comp)
    .join(" ");
}
```

- `sum()`이라는 내부함수로 자릿수마다 더해주는 처리를 해주고 그 리턴값을 `sort()`의 compareFunction(`comp()`)에 활용하면서 아름다운 코드를 완성했다. 공백을 제거해주고 문자를 걸러내는 과정 없이.
- `+` 연산자를 써서 문자열을 숫자로 변환했더니 코드가 훨씬 깔끔해보인다. `+` 연산자는 숫자가 아닌 값에 적용하면 `Number()`와 동일한 결과를 리턴한다.(라고 블로그에 정리해놨었는데.. 반성하고 앞으로 기회가 될 때 마다 활용해봐야겠다.)

<br />

## 기타 배운점 / 느낀점

- 숫자를 문자처럼 취급해서 정렬할 수 있는 신박한 메소드를 배웠다.  
  바로 [String.prototype.localeCompare()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare).

```javascript
// The letter "a" is before "c" yielding a negative value
"a".localeCompare("c"); // -2 or -1 (or some other negative value)

// Alphabetically the word "check" comes after "against" yielding a positive value
"check".localeCompare("against"); // 2 or 1 (or some other positive value)

// "a" and "a" are equivalent yielding a neutral value of zero
"a".localeCompare("a"); // 0
```

활용 예시야 다양하겠지만, 이번처럼 `sort()`의 매개변수인 compareFunction 내부에서 분기처리를 하다가 특정 조건에서 값을 비교하지 않고 순수하게 문자별로 비교하여 정렬하고 싶을때 즉, `2, 11, 11, 2000`이나 `2000, 11, 11, 2`가 아닌 `11, 11, 2, 2000`를 얻고 싶을때 `str.localeCompare(str)`를 유용하게 쓸 수 있겠다.
