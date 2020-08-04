# [Special String Again](https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings)

> Medium

<br />

## 문제 이해

string이 아래의 두 경우 중 하나일 경우 special string이라고 한다.

1. 모든 문자가 같은 경우 (e.g. "aaa")
2. 가운데에 위치한 문자를 제외한 나머지가 같을 경우 (e.g. "aadaa")

문자열 하나를 인자로 받고 그 안에서 **special string에 해당하는 substring의 갯수**가 몇 개인지 반환하는 문제이다.

<br />

## 코드 구현 & 풀이 학습

구현

```js
function updateMap(map, key) {
  const value = map.get(key);
  map.set(key, value ? value + 1 : 1);
}

function substrCount(n, s) {
  const subStr = new Map();
  for (let i = 0; i < n; i++) {
    updateMap(subStr, s[i]);
    for (let j = i + 1; j < n; j++) {
      updateMap(subStr, s.slice(i, j + 1));
    }
  }

  let result = 0;
  for (const [key, value] of subStr) {
    const length = key.length;
    if (length === 1) {
      result += value;
      continue;
    }

    const unique = new Set(key);
    if (unique.size === 1) {
      result += value;
      continue;
    }

    if (length % 2 && unique.size === 2) {
      const mid = Math.floor(length / 2);
      if (key[0] === key[mid + 1] && key[mid] !== key[mid + 1]) {
        result += value;
      }
    }
  }

  return result;
}
```

문자열을 순회하면서 문자열에서 나올 수 있는 모든 substring을 구한 후 Map에 그 빈도수를 맵핑했다.

> 예를 들어 "aaaa"의 모든 substring을 구하고 그 빈도수를 맵핑하면 다음과 같다.
>
> ```js
> Map { 'a' => 4, 'aa' => 3, 'aaa' => 2, 'aaaa' => 1 }
> ```

이렇게 만들어진 Map을 순회하면서 key값(substring)의 길이를 기준으로

- 길이가 1인 경우 무조건 special string이기 때문에 value(빈도수)를 `result`에 더해주고,
- 길이가 1이 아닌 경우 special string인 2가지 경우를 각각 분기처리하여 조건을 충족할 경우 value를 `result`에 더해주었다.
  1. substring이 하나의 문자로 이루어진 경우(= Set의 길이가 1)
  2. 길이가 홀수이면서 2가지 종류의 문자로 이루어져있으며(= Set의 길이가 2) 가운데 문자만 다른 경우

위 코드를 제출해보니 시간초과로 인해 대부분의 테스트를 통과하지 못했다.

<br />

풀이 학습

```js
function substrCount(n, s) {
  let counter = 0;

  for (let i = 0; i < n; i++) {
    counter++; // substring의 길이가 1인 경우 무조건 +1
    for (let j = i + 1; j < n; j++) {
      if (s[i] !== s[j]) {
        if (s.slice(i, j) === s.slice(j + 1, 2 * j - i + 1)) {
          counter++; // 가운데 문자(s[j])를 기준으로 양 옆이 같을 경우 +1
        }
        break;
      } else {
        counter++; // 같은 문자일 경우 +1
      }
    }
  }

  return counter;
}
```

이중 for문을 돌면서 substring의 조합을 구하면서 다음과 같이 special string의 조건을 충족하는 3가지 경우에 한해 `counter`를 1씩 더해준다.

- substring의 길이가 1인 경우 - e.g. `a`
- `s[i] !== s[j]`일때 가운데 문자 `s[j]`를 기준으로 양 옆이 같을 경우 - e.g. `aabaa`
- `s[i] === s[j]`인 경우 - e.g. `aaa`

순회를 하다가 다른 문자가 나왔을 때에만 양 옆을 비교해서 special string 여부를 판별하고 그 외에는 계속해서 `counter`를 1씩 더해주는 식이다.

<br />

중요 포인트

1. 양 옆을 비교할때 slice 메서드의 두 번째 인자인 endIndex를 구하는 규칙 (`2 * j - i + 1`)을 찾는 것
2. `break`문의 역할을 이해하는 것
   - `counter`가 중복해서 더해지지 않도록 해줌  
     예를 들어 "asasd"에서 `[i, j]`가 `[0, 1]`일때 `asa`로 인해 `counter`가 1 더해진 경우 `break`문이 없다면 `[i, j]`가 `[0, 2]`가 되고 `s[i] === s[j]` 조건이 **true**가 되면서 `counter`를 중복해서 더해주게됨
   - 순회를 즉시 종료시키고 코드의 성능을 높여줌

<br />

---

- [HackerRank - Special String Again](https://www.youtube.com/watch?v=fib2sRjlxuw)
