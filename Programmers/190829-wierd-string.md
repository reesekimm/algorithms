### lv.1 / Javascript

# [이상한 문자 만들기](https://programmers.co.kr/learn/courses/30/lessons/12930)

## 문제

문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

<br />

#### 제한 조건

- 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
- 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
- 공백은 문자열 앞 뒤에도 있을 수 있으며 한번에 두 개 이상 존재할 수 있습니다.
- 리턴 시 기존 공백의 위치 및 갯수가 보존되어야 합니다.

```
예) "　　　A aaaa AA a a a A Aaaaaaaaaa　AAa　　AAAAA　"
```

<br />

#### 입출력 예

|                       s                       |                   return                   |
| :-------------------------------------------: | :----------------------------------------: |
|               "try hello world"               |             "TrY HeLlO WoRlD"              |
| "　　 A aaaa AA a a a A Aaaaaaaaaa 　 AAa 　" | "　　 A AaAa Aa A A A A AaAaAaAaAa AaA 　" |

<br />

#### 입출력 예 설명

try hello world는 세 단어 try, hello, world로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 TrY, HeLlO, WoRlD입니다. 따라서 TrY HeLlO WoRlD 를 리턴합니다.

<br />

## 문제 해결

1. 인자로 받은 문자열을 `split`하여 베열 `arr`로 변환한다.
2. `arr`에 loop를 돌면서 문자가 등장할 때마다 임의의 배열 `tmp`에 해당 문자를 인덱스 정보와 함께 저장한다.  
   -> 예) tmp = [[3, 'r'], [4, 'T'], [5, 'y']]
3. 공백이 등장하거나 loop가 종료됐을 경우 `tmp`에 있는 정보를 처리한다.  
   -> 짝수 인덱스는 대문자로 바꾸고 홀수 인덱스는 소문자로 바꿔서 `arr`의 기존 위치에 대입
4. `arr`를 다시 문자열로 변환하여 리턴한다.

<br />

## 코드 구현

```javascript
function toWeirdCase(s) {
  var arr = s.split("");

  var tmp = [];
  for (var i = 0; i <= arr.length; i++) {
    if (arr[i] === " " && !tmp.length) {
      continue;
    } else if ((arr[i] === " " || i === arr.length) && tmp.length) {
      tmp.forEach((el, idx) => {
        idx % 2
          ? (arr[el[0]] = el[1].toLowerCase())
          : (arr[el[0]] = el[1].toUpperCase());
      });
      tmp.length = 0;
    } else {
      tmp.push([i, arr[i]]);
    }
  }

  return arr.join("");
}
```

인자에 `" A aaaa AA a a a A Aaaaaaaaaa AAa AAAAA "`를 대입하고 `performance.now()`를 사용해서 속도를 측정해보니 **0.76ms**가 나왔다.

<br />

## 다른 풀이

---

※ 아래 표기된 '코드 수행 시간'은 위와 동일한 대입인자 & 측정 도구를 사용해서 측정한 값이다.

---

### Solution 1

```javascript
function toWeirdCase(s) {
  var result = "";
  var num = 0;

  for (var i = 0; i < s.length; i++) {
    if (s.charAt(i) === " ") {
      num = 0;
      result += " ";
      continue;
    } else if (num % 2 === 0) {
      result += s.charAt(i).toUpperCase();
      num++;
    } else {
      result += s.charAt(i).toLowerCase();
      num++;
    }
  }
  return result;
}
```

코드 수행 시간 : **0.31ms**

- 문자열 <-> 배열 변환 과정이 없다.
- `num`이라는 변수를 써서 기존 문자열 안에서 공백이 아닌 문자만의 인덱스를 핸들링했다. (신박하다..!)

<br />

### Solution 2

```javascript
function toWeirdCase(s) {
  var result = "";

  for (var word of s.split(" ")) {
    for (var i in word) {
      result += word[i][
        parseInt(i) % 2 === 0 ? "toUpperCase" : "toLowerCase"
      ]();
    }
    result += " ";
  }

  return result.slice(0, -1);
}
```

코드 수행 시간 : **0.69ms**

- `for..of`로 문자열 안에서 문자chunk(`word`)를 걸러낸 뒤, 각각의 `word`에 대해 `for..in`을 써서 인덱스에 따른 대소문자 변환을 해줬다.
- 인덱스 위치에 조건문을 대입한 후 method명을 문자열로 리턴해서 함수를 실행했다. 함수를 이렇게 호출할 수도 있다니..

`for..in`, `for..of`를 자유자재로 활용하고 참신한 방법으로 함수를 호출한 점이 인상깊다. 기억해놨다가 나중에 활용해 봐야지! :)

<br />

### Solution 3

```javascript
function toWeirdCase(s) {
  return s
    .split(" ")
    .map(v =>
      v
        .split("")
        .map((v2, i2) => (i2 % 2 === 0 ? v2.toUpperCase() : v2.toLowerCase()))
        .join("")
    )
    .join(" ");
}
```

코드 수행 시간 : **0.46ms**

- 별도의 control flow 없이 `split`, `map`, `join`만으로 깔끔하게 처리했다b
