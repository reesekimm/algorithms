# [Sherlock and the Valid String](https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings&isFullScreen=true)

> Medium

<br />

## 문제 이해

문자열을 이루는 모든 문자의 등장횟수(frequency)가 동일하거나, 1개의 문자를 지웠을때 동일해질 수 있다면 유효한 문자열이라고 판별한다.
문자열을 인자로 받아서 위와 같은 조건으로 판별한 뒤 "YES" 또는 "NO"를 반환하면 된다.

<br />

## 코드 구현 & 풀이 학습

1차

```js
function isValid(s) {
  if (s.length === 1) return "YES";
  const table = new Map();

  for (let i = 0, len = s.length; i < len; i++) {
    const frequency = table.get(s[i]);
    table.set(s[i], frequency ? frequency + 1 : 1);
  }

  const values = [...table.values()].sort();
  let changed = false;
  let same = false;
  let sameAgain = false;

  for (let i = 0, len = values.length; i < len - 1; i++) {
    const diff = Math.abs(values[i] - values[i + 1]);
    if (diff > 1) return "NO";
    if (diff === 0) {
      if (!changed) {
        same = true;
      } else {
        if (same) {
          return "NO";
        } else {
          same = true;
        }
      }
    }
    if (diff === 1) {
      if (!changed) {
        changed = true;
      } else {
        return sameAgain ? "NO" : "YES";
      }
    }
  }
  return sameAgain ? "NO" : "YES";
}
```

문자열을 이루는 각각의 문자가 몇번씩 등장하는지를 `{"a" => 3, "b" => 2, ...}` 의 형태로 Map에 맵핑해두고 다시 빈도수만 배열로 추출해서 `[3, 2, ...]` 정렬한뒤 바로 다음 요소와의 차이(`diff`)를 절대값으로 비교해가면서 답을 도출하고자 했다.

위 코드로 "aabbccddeeffg"와 같이 하나의 문자가 딱 1번 차이나는 경우는 통과했지만 그 외에 3개의 test를 통과하지 못했는데, 다음과 같은 경우여서 파악이 어려웠다.

```
"ebhcgicceggecgdcibbeicigehhebabiehbdgaeaigihghbhigihfebgabicbgfhhedgbfehiahchcecedffhccebifcbdfcfaecicafahfiecceeaabbecfhgbfifabbffadcieeaiidddhfdeccaedbgcfdehbadihheieidgcfbdiiicgahebfbbdfeffegbdhgdagefhbgafaabfghdcbfdhabhfahbdhgifbghhafcieachcbeabccbiigdcfegcccfafehegbiecbdhabcffggiifaabfagbfdfbfacdcafabccgibiidgabiabigbgbbaideeagaaffcddhieicehhchfedfgbgbfhgedhacegaieeedggacbbgadeibbbcdhbabbieibcfbhgdbbiecdhbffaghh"...
```

풀이를 학습하고 정리하기로 결정.

<br />

2차 (풀이 학습)

```js
function isValid(s) {
  let fq = {};
  s.split("").map((v) => (fq[v] ? (fq[v] += 1) : (fq[v] = 1)));

  let c = 0;
  Object.keys(fq).map((v, i, a) => (fq[v] !== fq[a[0]] ? c++ : 1));

  return c > 1 ? "NO" : "YES";
}
```

`fq`라는 객체를 생성하고 문자열을 이루는 문자들의 등장 횟수를 맵핑했다. 여기까지는 나의 풀이와 접근 방식이 같은데, 그 다음이 중요하다. `fq`객체에서 key값들을 배열에 담은 뒤 map 메서드를 사용하여 순회하면서 **첫번째 문자(첫번째 key값)를 기준으로** 문자열을 이루는 모든 문자와 등장 횟수를 비교해나가고 그 차이가 같은지 다른지만 판별해서 다르면 무조건 `c`를 1을 더해주는 것이다.

이 풀이의 핵심은 기준점을 첫번째 문자로 고정했다는 점인 것 같다. 굳이 배열을 정렬할 필요도 없었고 순회하면서 기준점을 계속해서 바꿔가면서 차이가 0인지 1인지 1보다 큰지 다양한 케이스를 고려할 필요가 없었다.

이 코드를 좀 더 개선해본다면 두번째 map 메서드 대신 for문을 사용해서 `c`값이 1을 초과하면 즉시 순회를 종료하고 값을 반환할 수 있을 것 같다.

```js
function isValid(s) {
  let fq = {};
  s.split("").map((v) => (fq[v] ? (fq[v] += 1) : (fq[v] = 1)));

  const chars = Object.keys(fq);
  let c = 0;
  for (let i = 0, len = chars.length; i < len; i++) {
    if (fq[chars[i]] !== fq[chars[0]]) c++;
    if (c > 1) return "NO";
  }

  return "YES";
}
```
