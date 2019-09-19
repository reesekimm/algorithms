### lv.2 / Javascript

# [가장 큰 수](https://programmers.co.kr/learn/courses/30/lessons/42746)

## 문제

0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

<br />

#### 제한 조건

- numbers의 길이는 1 이상 100,000 이하입니다.
- numbers의 원소는 0 이상 1,000 이하입니다.
- 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

<br />

#### 입출력 예

|      numbers      |  return   |
| :---------------: | :-------: |
|    [6, 10, 2]     |  "6210"   |
| [3, 30, 34, 5, 9] | "9534330" |

<br />

## 문제 해결

1. 주어진 수가 전부 0인 경우 "0"을 리턴하도록 분기 처리를 한다.
2. 0이 포함된 숫자와 그렇지 않은 숫자를 각각 새로운 배열에 나눠 담고 정렬해준다.
3. 0은 또다른 배열에 0끼리 모았다가 문자열로 변환하기 전에 다른 두 배열과 합친다.
4. 세 개의 배열을 합친 후 문자로 변환하여 리턴한다.

<br />

## 코드 구현

```js
function solution(numbers) {
  var withoutZero = [];
  var withZero = [];
  var zeros = [];

  if (numbers.every(num => num === 0)) return "0";

  numbers.forEach(num =>
    (num + "").includes("0")
      ? num + "" === "0"
        ? zeros.push(num + "")
        : withZero.push(num + "")
      : withoutZero.push(num + "")
  );

  withoutZero.sort().reverse();
  withZero.sort((a, b) => {
    let lenA = a.length;
    let lenB = b.length;
    if (lenA > lenB) {
      return 1;
    } else if (lenA < lenB) {
      return -1;
    } else {
      return lenB - lenA;
    }
  });

  return withoutZero.concat(withZero, zeros).join("");
}
```

<br />

## 결과

샘플테스트는 모두 통화했으나  
<img src="https://user-images.githubusercontent.com/42695954/65135712-5b3d8a80-da41-11e9-91a4-f05b0707fe99.PNG" alt="example test" width="400"/>

랜덤테스트 결과는 처참했다..  
<img src="https://user-images.githubusercontent.com/42695954/65135892-ace61500-da41-11e9-9cda-088482add124.PNG" alt="random test" width="300"/>

<br />

그런데 질문 게시판을 둘러보다가 아래 글과 함께 힌트를 발견했다.  
<img src="https://user-images.githubusercontent.com/42695954/65142658-297ef080-da4e-11e9-9270-4637dc4c8089.PNG" alt="qna" width="500">

- 힌트

12의 경우에는 12가 반복되어 1212(1212...)  
121의 경우에는 121이 반복되어 1211(21121...)

1212 > 1211  
2121 < 2122

<br />

> 힌트 적용해서 테스트해보기

```
[6, 10, 2] → [6666, 1010, 2222] → [6666, 2222, 1010] → [6, 2, 10] → "6210"

[3, 30, 34, 5, 9] → [3333, 3030, 3434, 5555, 9999] → [9999, 5555, 3434, 3333, 3030] → [9, 5, 34, 3, 30] → "9534330"

[102, 22, 80, 12] → [1021, 2222, 8080, 1212] → [8080, 2222, 1212, 1021] → "802212102"
```

4자리 수를 만들어서 비교 후 정렬하니 올바른 답이 나온다.  
원리를 생각해봤을때 일단 주어진 숫자가 0 이상 1000 이하이기 때문에 4자리 숫자를 만들면 1000은 0보다는 크지만 그 외의 경우에는 항상 작은 수로 판별되고 정렬 시 가장 오른쪽에 위치하게 되기 때문인듯 하다.

<br />

## 코드 구현 (2차)

```js
function solution(numbers) {
  if (numbers.every(num => num === 0)) return "0";
  return numbers
    .sort((a, b) => {
      let repeatedA = (a + "").repeat(4).slice(0, 4);
      let repeatedB = (b + "").repeat(4).slice(0, 4);
      return repeatedB - repeatedA;
    })
    .join("");
}
```

모든 테스트에 통과했다. 하지만 다른 사람이 알려준 방향대로 코드구현만 하고 내가 푼 문제가 아닌듯한 느낌이다ㅠㅠ 반성하자..

<br />

## 다른 솔루션 분석

```js
function solution(numbers) {
  var answer = numbers
    .map(v => v + "")
    .sort((a, b) => (b + a) * 1 - (a + b) * 1)
    .join("");

  return answer[0] === "0" ? "0" : answer;
}
```

- sort 메서드의 compareFunc에서 문자열 끼리 더해주고 `* 1`을 함으로써 숫자로 변환하여 크기비교를 했다. `*`를 써서 문자열을 숫자로 바꿀 수 있다니.. 새롭게 알게 되었다.
- return문에서 문자열 answer의 첫번째 문자가 "0"일 경우 "000"이 아닌 "0"이 리턴되도록 한 점도 영리한 방법인 것 같다.
