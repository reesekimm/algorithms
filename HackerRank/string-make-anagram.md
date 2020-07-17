# [Strings: Making Anagrams](https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings)

> Easy

<br />

## 문제 이해

두 개의 문자열을 인자로 받고 anagram을 만들기 위해 지워야 할 문자의 갯수를 구하는 문제이다.

<br />

## 코드 구현 & 풀이 학습

```js
function makeAnagram(strA, strB) {
  const table = new Map();
  const a = "a",
    b = "b",
    both = "both";

  for (const letter of strA) {
    // O(n)
    const value = table.get(letter);
    table.set(letter, value ? [a, value[1] + 1] : [a, 1]);
  }

  for (const letter of strB) {
    // O(m)
    const value = table.get(letter);
    value
      ? value[0] === b
        ? table.set(letter, [b, value[1] + 1])
        : table.set(letter, [both, value[1] - 1])
      : table.set(letter, [b, 1]);
  }

  return [...table.values()].reduce((result, curr) => {
    // O(n + m) (worst)
    result += curr[0] === both ? Math.abs(curr[1]) : curr[1];
    return result;
  }, 0);
}

// Total : O(n + m)
```

첫번째 인자로 받은 `strA`를 이루는 각 문자의 frequency를 맵핑한 후, 두번째 인자인 `strB`를 순회하면서 출처와 frequency를 업데이트 해나갔다.

여기서 출처란 '해당 문자가 어떤 문자열에서 등장하는가'를 의미한다. 예를들어 `"k": ["a", 2]`는 문자 k가 strA에서 2번 등장했다는 뜻이다.

strB를 순회하면서 strA에서 등장했던 문자의 경우 출처를 `both`로 변경한 후 frequency를 하나 차감해주고, strA에 등장하지 않았던 문자의 경우 출처를 `b`로 표기하여 맵에 추가해준다.

마지막으로 모든 frequency를 누적 합산 해주면 되는데, 이때 출처가 `both`인 경우는 절대값으로 처리해준다. 문자가 `strA`보다 `strB`에서 더 자주 등장했을 경우 해당 frequency가 마이너스 값을 가지기 때문.

시간복잡도는 **O(n + m)** 이다.
