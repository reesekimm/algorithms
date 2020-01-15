### lv.1 / Javascript

# [K번째 수](https://programmers.co.kr/learn/courses/30/lessons/42748)

## 문제

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

<br />

#### 제한사항

array의 길이는 1 이상 100 이하입니다.<br />
array의 각 원소는 1 이상 100 이하입니다.<br />
commands의 길이는 1 이상 50 이하입니다.<br />
commands의 각 원소는 길이가 3입니다.

<br />

#### 입출력 예

| array                 |             commands              |    return |
| --------------------- | :-------------------------------: | --------: |
| [1, 5, 2, 6, 3, 7, 4] | [[2, 5, 3], [4, 4, 1], [1, 7, 3]] | [5, 6, 3] |

<br />

#### 입출력 예 설명

[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.<br />
[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.<br />
[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.

<br />

## 코드 구현 (1차 - 190812)

```javascript
function solution(array, commands) {
  var result = [];

  for (var i = 0; i < commands.length; i++) {
    var temp = array
      .slice(commands[i][0] - 1, commands[i][1])
      .sort((a, b) => a - b);
    result.push(temp[commands[i][2] - 1]);
  }

  return result;
}
```

1. 자르고(`slice`) & 정렬한다(`sort`)
2. 찾고자 하는 인덱스의 요소를 임의의 result 배열에 push 한다.

문제에서 '~번째'라고 언급하는 순서가 배열의 index와 매치될 수 있도록 신경쓴다.<br />
(e.g. 배열의 3번째 요소 => index가 2다.)

<br />

## 코드 구현 (2차 - 200115)

```js
function solution(array, commands) {
  return commands.map(cmd => {
    const [i, j, k] = cmd;
    const processedArr = array.slice(i - 1, j).sort((a, b) => a - b);
    return processedArr[k - 1];
  });
}
```

- 클로저와 map 메서드를 활용하여 다시 한 번 풀어보았다.
- 코드의 길이 보다는 논리적인 흐름이 잘 드러나는 명시적인 코드를 작성하는데에 초점을 맞췄다.
- 예전에는 다른 사람들의 풀이를 공부하면서 그냥 그런가보다 하고 넘어갔었던 부분들(클로저, 고차함수)을 이제는 스스로 이해하고 코드로 작성할 수 있게 되었다:)

<br />

## 코드 분석 (190812)

1.

```javascript
function solution(array, commands) {
  return commands.map(v => {
    return array
      .slice(v[0] - 1, v[1])
      .sort((a, b) => a - b)
      .slice(v[2] - 1, v[2])[0];
  });
}
```

commands에 `map`을 써서 `map`이 생성한 새로운 배열을 바로 리턴했다는 점이 인상깊다. `map`을 호출한 객체(문제에서는 commands)의 각각의 요소에 대해 callback을 실행하는데 이때 **callback에 의해 변경되는 대상이 꼭 그 객체(commands)가 될 필요는 없다**는게 핵심인 것 같다. 나는 여태 `map`을 호출한 객체를 변경하기 위해 `map`을 썼는데, `map`을 충분히 이해하지 못하고 `map`이 가진 기능의 일부만 써왔던거다. 앞으로는 `map`을 비롯한 다른 메소드들 좀 더 다양하게 활용해봐야 겠다는 생각이 들었다. 이걸 실천하기 위해서는 코드를 많이 보고 많이 써봐야겠지.

<br />

2.

```javascript
function solution(array, commands) {
  return commands.map(
    ([from, to, k]) => array.slice(from - 1, to).sort((x, y) => x > y)[k - 1]
  );
}
```

- Destructuring을 활용해서 cammands의 각각의 요소를 `[from, to, k]`와 같이 명시적으로 표기했다.
- `sort`를 쓸 때 부등호를 사용할 수 있다는 것도 알게됐다.
- 1번 솔루션과 다르게 `slice`를 2번 쓰지 않고 [k - 1]로 바로 요소에 접근한 점도 좋다.

<br />

## 기타 느낀점 (190812)

- 쉬운 문제일수록 어떻게 하면 더 효율적/효과적으로으로 풀 수 있을지 고민해보는 시간을 충분히 가져야겠다.
- 문제가 default로 제시하는 포맷에 얽매이지 말자. 좀 더 좋은 접근방법을 떠올리는 데 제약이 될 수 있다.
  예를들면 이런거..

```javascript
function solution(array, commands) {
  var answer = [];
  return answer;
}
```
