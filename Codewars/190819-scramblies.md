### 5kyu / Javascript

# [Scramblies](https://www.codewars.com/kata/scramblies/train/javascript)

## 문제

Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

<br />

#### Notes

- Only lower case letters will be used (a-z). No punctuation or digits will be included.
- Performance needs to be considered

```
Input strings s1 and s2 are null terminated.
```

<br />

#### Examples

```
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
```

<br />

## 문제 이해

문자열 `str1`과 문자열 `str2`를 인자로 받는 함수를 작성한다.  
`str1`에 있는 문자들을 사용해서 `str2`를 만들 수 있으면 `true`를 리턴하고, 만들 수 없으면 `false`를 리턴한다.  
`str1`과 `str2`는 영어 소문자로만 이루어져 있다. ([구두점](https://www.merriam-webster.com/dictionary/punctuation%20mark), 숫자는 미포함)

> 성능을 고려해서 코드를 작성할 것 !

<br />

## 코드 구현

#### 1차

```javascript
function scramble(s1, s2, n) {
  // 1.
  if (!n) {
    if (s2.length === 1) {
      return s1.includes(s2);
    }
    if (s1.length < s2.length) {
      return false;
    }
    s1 = s1
      .split("")
      .sort()
      .join("");
    s2 = s2
      .split("")
      .sort()
      .join("");
  }

  // 2.
  var checkFirst = s1.indexOf(s2[0]);
  var checkLast = s1.lastIndexOf(s2[s2.length - 1]);
  if (checkFirst < 0 || checkLast < 0) {
    return false;
  }

  // 3.
  var s1Sliced = s1.slice(checkFirst + 1, checkLast);
  var s2Sliced = s2.slice(1, s2.length - 1);

  // 4.
  return s2Sliced.length ? scramble(s1Sliced, s2Sliced, 1) : true;
}
```

1. 함수 최초 실행 시,  
   ▷ `str2`의 길이가 1인 경우 `includes` 사용하여 true/false 리턴
   ▷ `str1`의 길이가 `str2`보다 짧을 경우 false 리턴
   ▷ `str1`과 `str2`를 `sort()`를 사용하여 정렬
2. 정렬된 `str2`의 첫번째/마지막 문자가 졍렬된 `str1`에 포함되어 있는지 확인  
   (첫번째 문자 확인시 `indexOf()` / 마지막 문자 확인시 `lastIndexOf()`를 사용한 이유는 3번에서 `str1`, `str2`를 가공할 때 쓰기 위함)
3. 포함되어 있을 경우 `str1`, `str2` slice 처리
4. `str2`의 길이가 0일 경우 true리턴 / 0이 아닐 경우 재귀  
   (매개변수 `n`의 위치에 1을 전달해서 재귀를 돌 때 1번 과정을 skip하도록 처리)

<br />

#### 2차

```javascript
function scramble(s1, s2) {
  var length1 = s1.length;
  var length2 = s2.length;

  if (length2 === 1) {
    return s1.includes(s2);
  }
  if (length1 < length2) {
    return false;
  }

  // convert str to arr
  s1 = s1.split("");
  s2 = s2.split("");

  for (let i = 0; i < length2; i++) {
    if (s1.includes(s2[i])) {
      s1.splice(s1.indexOf(s2[i]), 1);
    } else {
      return false;
    }
  }

  return true;
}
```

배열로 변환하여 loop를 돌면서  
`str2`의 문자가 `str1`에 포함되어 있을 경우 `str1`에서 해당 문자를 `splice`하여 삭제

---

1차와 2차 모두, 길이가 매우 긴 문자를 처리할 때 `Execution Timed Out`이 발생했다ㅠㅠ
성능 최적화를 어떻게 해야 할지 좀 더 고민해봐야 겠다.

<br />

## 다른 방법

<br />

## 기타 느낀점
