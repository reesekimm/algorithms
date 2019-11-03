### 5kyu / Javascript

# [Caesar Cipher Helper](https://www.codewars.com/kata/caesar-cipher-helper/javascript)

## Challenge

Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.

For example, given an input such as this:

```
var c = new CaesarCipher(5); // creates a CipherHelper with a shift of five
c.encode('Codewars');        // returns 'HTIJBFWX'
c.decode('BFKKQJX');         // returns 'WAFFLES'
```

If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
The shift will always be in range of `[1, 26]`.

<br/>

## 문제 이해

알파벳 문자열을 암호화하거나 해독하는 클래스를 작성하는 문제이다.

알파벳이 `A, B, C, D, E, F, G, H, I, J, K, L, ...`순차적으로 있을 때 암호화/해독 방법은 다음과 같다.

- 암호화 : 알파벳을 기존 위치에서 특정 숫자만큼 오른쪽(순차적)으로 이동한 위치의 문자로 변환한다.
- 해독 : 특정 숫자만큼 왼쪽(역순)으로 이동한 위치의 문자로 변환한다.

```
var c = new CaesarCipher(5); // creates a CipherHelper with a shift of five
c.encode('Codewars');        // returns 'HTIJBFWX'
c.decode('BFKKQJX');         // returns 'WAFFLES'
```

위 예시에서 알 수 있듯이 암호화할때 순차적으로 이동하다가 Z를 넘어가게되면 다시 A로 돌아와서 마저 이동을 해야하고, 해독할때 A보다 왼쪽으로 넘어가면 Z로 넘어가서 마저 이동 해야한다.

따라서 `W`를 5만큼 이동해서 '암호화'하면 `B`가 되고, `(W) → X → Y → Z → A → B`<br/>
반대로 `B`를 5만큼 이동해서 '해독'하면 `W`가 된다. `W ← X ← Y ← Z ← A ← (B)`

> **참고**
> 암호화/해독시 리턴값은 항상 대문자여야 한다.
> 문자열에 알파벳이 아닌 다른 문자 (문장부호, 띄어쓰기 등)가 있을 경우 변환하지않고 그대로 리턴해준다.
> 이동(shift) 범위는 1 이상 26 이하이다.

<br/>

## 코드 구현

```js
var CaesarCipher = function(shift) {
  this.shift = shift;
};

CaesarCipher.prototype.encode = function(code) {
  let encoded = "";
  let uppered = code.toUpperCase();
  for (let i = 0, len = code.length; i < len; i++) {
    let charCode = uppered.charCodeAt(i);
    let newCode = charCode + this.shift;
    if (charCode > 64 && charCode < 91) {
      if (newCode >= 91) {
        newCode = newCode - 90 + 64;
      }
      encoded += String.fromCharCode(newCode);
    } else {
      encoded += uppered[i];
    }
  }
  return encoded;
};

CaesarCipher.prototype.decode = function(code) {
  let decoded = "";
  for (let i = 0, len = code.length; i < len; i++) {
    let charCode = code.charCodeAt(i);
    let newCode = charCode - this.shift;
    if (charCode > 64 && charCode < 91) {
      if (newCode <= 64) {
        newCode = 90 - (64 - newCode);
      }
      decoded += String.fromCharCode(newCode);
    } else {
      decoded += code[i];
    }
  }
  return decoded;
};
```

- encode, decode를 CaesarCipher.prototype의 메서드로 할당하는 방법을 선택했다.
- 알파벳의 대문자 여부를 판별하고 변환할 알파벳을 찾는데 `charCodeAt` 메서드를 사용했다.

**부족한점 / 개선 포인트**

- `encode`와 `decode`는 알파벳을 변환하는 부분만 빼고 동일한 흐름이기 때문에 대부분의 코드가 중복이다. (중복을 줄일 수 있는 방법이 뭐가 있을까..)
- 암호화할때 Z를 넘어가는경우, 해독할때 A를 넘어가는 경우를 따로 분기처리 하지 않고 문제를 해결할 수 있는 방법을 고민하다가 답안을 제출했다. 수학적 사고력이 필요한 부분인데 이부분이 부족하다고 느꼈다.
- encoded, decoded, charCode, newCode.. 변수를 굉장히 많이 생성했다. 코드를 간결하게 하기 위한 목적이지만 아직 개선의 여지는 충분한 것 같다.

<br/>

## 다른 풀이 분석

### 1.

```js
var CaesarCipher = function(shift) {
  var a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  this.encode = function(str) {
    return str.replace(/[a-z]/gi, function(s) {
      return a[(a.indexOf(s.toUpperCase()) + shift) % 26];
    });
  };
  this.decode = function(str) {
    return str.replace(/[a-z]/gi, function(s) {
      return a[(a.indexOf(s.toUpperCase()) + 26 - shift) % 26];
    });
  };
};
```

- encode, decode를 prototype 객체에 할당하지 않고 생성자 함수에 직접 넣어주었다.
- `replace`에 정규표현식을 써서 문자열을 이루는 모든 문자에 대해 대문자로 변환한 뒤 암호화 또는 해독 처리를 했다.
- 알파벳을 변환할 때 대문자 알파벳 전체를 문자열 형태로 변수에 담아뒀다가 indexOf로 변활할 알파벳을 찾아가는 식인데, `charCodeAt`메서드를 썼을 때보다 코드가 간결하다.
- decode의 경우 인자로 받는 문자가 이미 대문자이기 때문에 대문자로 변환해주는 과정을 생략해도 된다.

### 2.

```js
var CaesarCipher = function(shift) {
  this.sh = shift;
};

CaesarCipher.prototype.encode = function(s, d) {
  r = "";
  s = s.toUpperCase();
  d = d || this.sh;
  for (i in s)
    r +=
      s[i] >= "A" && s[i] <= "Z"
        ? String.fromCharCode(((s.charCodeAt(i) - 65 + d) % 26) + 65)
        : s[i];
  return r;
};

CaesarCipher.prototype.decode = function(s) {
  return this.encode(s, 26 - this.sh);
};
```

- 함수 하나로 `encode`와 `decode`를 모두 처리함으로써 코드의 중복을 최소화했다. (encode, decode시에 모두 적용할 수 있도록 변환할 문자를 계산하는 부분 (`((s.charCodeAt(i) - 65 + d) % 26) + 65`)은 정말 대단한것 같다..)
- 대문자 알파벳인지 여부를 판별할 때 `charCodeAt`메서드를 쓰지 않고 `s[i] >= "A" && s[i] <= "Z"` <- 이렇게 마치 숫자처럼 대소비교를 했다는 점도 인상깊다. 문자끼리 대소비교가 된다니! 자바스크립트가 이정도로 유연한 언어인줄 몰랐다.
- 하지만 문자열을 순회할 때 `for...in`을 사용한 건 좋은 접근이 아니다. `for...in`은 순회하는 요소의 순서를 보장하지 못하기 때문에 이 문제처럼 알파벳의 순서가 중요한 경우에는 적합하지 않다.
- 변수명이 지나치게 축약되어 있어서 코드의 가독성이 떨어진다는점 역시 아쉽다. `r` -> `result`, `s` -> `string` 같이 좀 더 명확하게 적어줬다면 더 좋았을 것 같다.
