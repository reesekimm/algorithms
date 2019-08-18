### lv.1 / Javascript

# [문자열 내 마음대로 정렬하기](https://programmers.co.kr/learn/courses/30/lessons/12915)

## 문제

문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 [sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.

<br />

#### 제한 조건

strings는 길이 1 이상, 50이하인 배열입니다.  
strings의 원소는 소문자 알파벳으로 이루어져 있습니다.  
strings의 원소는 길이 1 이상, 100이하인 문자열입니다.  
모든 strings의 원소의 길이는 n보다 큽니다.  
인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.

<br />

#### 입출력 예

|      strings      |  n  |      return       |
| :---------------: | :-: | :---------------: |
|  [sun, bed, car]  |  1  |  [car, bed, sun]  |
| [abce, abcd, cdx] |  2  | [abcd, abce, cdx] |

<br />

#### 입출력 예 설명

[입출력 예 1]  
sun, bed, car의 1번째 인덱스 값은 각각 u, e, a 입니다. 이를 기준으로 strings를 정렬하면 [car, bed, sun] 입니다.

[입출력 예 2]  
abce와 abcd, cdx의 2번째 인덱스 값은 c, c, x입니다. 따라서 정렬 후에는 cdx가 가장 뒤에 위치합니다. abce와 abcd는 사전순으로 정렬하면 abcd가 우선하므로, 답은 [abcd, abce, cdx] 입니다.

<br />

## 코드 구현

```javascript
function solution(strings, n) {
  function compare(a, b) {
    if (a[n] < b[n]) {
      return -1;
    } else if (a[n] > b[n]) {
      return 1;
    } else {
      return a.localeCompare(b);
    }
  }
  return strings.sort(compare);
}
```

<br />

## 다른 풀이

```javascript
function solution(strings, n) {
  return strings.sort((a, b) =>
    a[n] === b[n] ? a.localeCompare(b) : a[n].localeCompare(b[n])
  );
}
```

내가 처음에 시도했던 풀이 방법이다. 나는 `a[n].localeCompare(b[n])` 위치에 `a - b`를 넣었다가 테스트코드를 통과하지 못해서 다른 방법으로 우회해서 풀었는데, `a - b`를 넣었다는건 내가 `sort()`나 `localeCompare()`을 정확하게 이해하고 있지 않았기 때문인 것 같다.  
`sort()`랑 `localeCompare()`은 날잡고 정리해서 정확하게 알고 넘어가야겠다!

```javascript
function solution(strings, n) {
  return strings.sort((a, b) => {
    const chr1 = a.charAt(n);
    const chr2 = b.charAt(n);

    if (chr1 == chr2) {
      return (a > b) - (a < b);
    } else {
      return (chr1 > chr2) - (chr1 < chr2);
    }
  });
}
```

`charAt()`을 쓸 수도 있다!
