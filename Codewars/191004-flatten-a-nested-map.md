### 5kyu / Javascript

# [Flatten a Nested Map](https://www.codewars.com/kata/52859abdf8fc1b12e0000141)

## Chanllenge

Write a function that takes a hierarchical map of properties and converts it to a single, flattened map, with the different levels separated by a forward slash ('/').

For example, given an input such as this:

```
{
  'a': {
    'b': {
      'c': 12,
      'd': 'Hello World'
    },
    'e': [1,2,3]
  }
}
```

return a new map:

```
{
  'a/b/c': 12,
  'a/b/d': 'Hello World',
  'a/e': [1,2,3]
}
```

The passed in argument will always be an object, but it may be empty. Make sure to correctly test for Arrays and nulls — they should be left as is in the result. The only property types will be:

- true
- false
- Numbers
- Strings
- null
- Arrays
- Functions
- Nested Maps

Keys can be any string of characters, excluding the '/' character.

<br />

## 문제 이해

여러 개의 depth로 이루어진 객체에 들어있는 값들을 새로운 객체에 옮기는 문제이다. 이때 각각의 값들은 기존 객체에서의 자신의 위치(path)를 키값으로 가진다.

Object Arg:

```
{
  'a': {
    'b': {
      'c': 12,
      'd': 'Hello World'
    },
    'e': [1,2,3]
  }
}
```

Expected Output:

```
{
  'a/b/c': 12,
  'a/b/d': 'Hello World',
  'a/e': [1,2,3]
}
```

<br />

## 풀이 방법

1. 함수가 리턴할 임의의 객체 `result`를 생성한다.
2. 객체를 순회한다. (재귀)

- 프로퍼티의 값이 객체(함수나 배열이 아닌 `{}`객체)일 경우
  1. 경로를 업데이트한다.
  2. 해당 객체를 순회한다.
- 프로퍼티의 값이 객체가 아닐 경우
  1. 경로를 업데이트한다.
  2. 해당 값을 경로와 함께 `result`에 새로운 프로퍼티로 할당한다.

3. 가장 깊은 depth에 있는 값까지 전부 탐색한 후 `result` 객체를 리턴한다.

---

#### [`{}`객체 여부를 판별하는 방법](https://stackoverflow.com/questions/8511281/check-if-a-value-is-an-object-in-javascript)

1. `Object.toString.call(value) === [object Object]`
2. `typeof value === "object" && !Array.isArray(value) && value !== null`
3. `JSON.stringify(value)[0] === "{"`

<br />

## 코드 구현

```javascript
function flattenMap(map, parent, result = {}) {
  for (let key in map) {
    let path = parent ? parent + "/" + key : key;

    typeof map[key] === "object" && !Array.isArray(map[key]) && map[key] !== null
      ? flattenMap(map[key], path, result)
      : (result[path] = map[key]);
  }
  return result;
}
```

원래 주어진 함수가 받는 인자는 map 하나밖에 없없다. 그런데 이 경우 재귀를 돌때마다 `result`객체와 `경로`를 리셋하지 않고 업데이트 해나가는 방법을 찾는게 어려웠다. 2시간을 고민하다가 결국 [stackoverflow](https://stackoverflow.com/questions/44134212/best-way-to-flatten-js-object-keys-and-values-to-a-single-depth-array)의 도움을 받아 `result`객체와 `경로`를 재귀 함수의 인자로 전달해서 해결했다.

<br />

## 다른 풀이 분석

### 1.

```javascript
function flattenMap(map) {
  var result = {};

  // 내부함수(재귀) 선언
  function recurse(cur, prop) {
    // 객체가 아닐 경우 result에 프로퍼티로 할당
    if (Object(cur) !== cur || Array.isArray(cur)) {
      return (result[prop] = cur);
    }
    // 객체일 경우 객체 순회하면서 재귀
    for (var p in cur) {
      recurse(cur[p], prop ? prop + "/" + p : p);
    }
  }

  // 내부함수 실행
  recurse(map, "");
  return result;
}
```

- `Object()`를 사용해서 객체여부를 판별했다.
  참고로 `Object()`는 인자로 객체/배열/함수를 받을 경우 해당 값을 그대로 리턴하지만 그 외 숫자나 문자열은 객체의 형태로 변환하여 리턴한다.

```javascript
let string = "hello";
let number = 123;
let func = function(){};
let obj = {name: "John", age: 30};
let arr = ["a", "b", 1];

Object(string);
// String {"string"}
0: "s"
1: "t"
2: "r"
3: "i"
4: "n"
5: "g"

Object(number); // Number {33}
Object(func);   // function(){};
Object(obj);    // {name: "John", age: 30}
Object(arr);    // ["a", "b", 1]
```

<br />

## 기타 배운것 / 느낀점

- 경로를 업데이트하는 방법을 찾다가 소소하게 정규표현식 [개념](https://stackoverflow.com/questions/10610402/javascript-replace-all-commas-in-a-string)을 알게됐다.
  `.`마침표는 `-` `--`와 같은 line terminator를 제외하고 모든 문자와 매치되기 때문에 마침표를 escape하고 싶으면 `/./`가 아니라 `/\./`literal을 써야 한다.

> 잘못된 방법

```javascript
var myStr = "this.is.a.test";
var newStr = myStr.replace(/./g, "-");

console.log(newStr); // "//////////////"
```

> 옳은 방법

```javascript
var myStr = "this.is.a.test";
var newStr = myStr.replace(/\./g, "-");

console.log(newStr); // "this-is-a-test"
```

- 재귀 / class / 자료구조 / HOF 와 관련된 알고리즘을 매주 하나씩 풀어봐야겠다
- 문제를 2시간 이내에 풀지 못할 경우 솔루션을 공부하면서 배우자:)
