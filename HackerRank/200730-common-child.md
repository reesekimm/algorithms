# [Common Child](https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings)

> Medium

<br />

## 문제 이해

영문 대문자로만 이루어져있고, 길이가 같은 문자열 두 개를 인자로 전달받는다.  
두 문자열에서 _동일하게 추출할 수 있는_ 가장 '긴' 문자열의 길이를 반환하는 문제이다.

```
ABCD
ABDC
```

위의 두 문자열에서 공통적으로 추출할 수 있는(common child) 가장 긴 문자열은 **ABC와 ABD**로, **3**을 반환하면 된다.  
주의할 점은 *인자로 받은 문자열을 재정렬할 수 없다*는 점이다. 그렇기 때문에 위 예시에서 ABCD는 common child가 될 수 없다.

<br />

## ~~코드 구현~~ & 풀이 학습

### Longest Common Subsequence (LCS) Dynamic Programming

> 재귀를 사용한 방식
> ![LCS - recursion](https://i.postimg.cc/xTfcLZXK/image.png)

> for loop을 사용한 방식
> ![LCS - for loop](https://i.postimg.cc/Hsg0NMzT/image.png)

```js
function commonChild(s1, s2) {
  const length1 = s1.length; // O(1)
  const length2 = s2.length; // O(1)
  if (length1 === 0 || length2 === 0) return 0;

  const memo = [];

  for (let i = 0; i <= length2; i++) {
    //O(m)
    memo.push(Array(length1 + 1).fill(0));
  }

  for (let i = 0; i < length1; i++) {
    // O(n * m)
    for (let j = 0; j < length2; j++) {
      if (s1[i] === s2[j]) {
        memo[i + 1][j + 1] = memo[i][j] + 1;
      } else {
        memo[i + 1][j + 1] = Math.max(memo[i + 1][j], memo[i][j + 1]);
      }
    }
  }

  return memo[length1][length2];
}

// 시간복잡도 : O(n * m)
// 공간복잡도 : O(n * m)
```

- 다이나믹 프로그래밍에 대해 학습하고 푼 첫 문제이다.  
  다이나믹 프로그래밍을 구현하는 여러가지 방법이 있었는데 이중 for문을 사용하는 방식이 가장 직관적이고 이해가 잘 가서 그 방식으로 풀었다.

- 0으로 채워진 이차원 배열 `memo`을 생성할때 다음과 같이 작성했었는데, 코드가 의도한대로 동작하지 않았다.

  ```js
  const memo = Array(length2 + 1).fill(Array(length1 + 1).fill(0));
  ```

  디버깅을 해보니 for문을 돌면서 내부의 값을 변경하면 memo 내부의 모든 배열이 변경됐다.  
  원인은 `Array(length1 + 1).fill(0)` <- 이 부분이었다.  
  배열은 객체이기 때문에 참조값이 전달된다. 위 코드대로라면 실직적으로 배열은 하나이고 그 배열을 참조하는 배열들로 `memo`를 채운 셈이다. 원인을 파악하고 나서 for문을 사용해서 매번 '새로운' 배열을 생성하여 `memo`를 채우도록 변경했다.

- 이 방식의 공간복잡도는 `O(n * m)`인데, 변수를 활용하면 O(n)으로 최적화할 수 있다.  
  다음주정도에 공간복잡도를 개선한 방식과 재귀를 사용하는 방식으로 다시 풀어봐야겠다.

<br />

> 참고 - [string 또는 array `.length`의 시간복잡도에 대하여](https://stackoverflow.com/a/32850687)

<br />

---

- [Longest Common Subsequence(LCS) Dynamic Programming In O(N) Space](https://www.youtube.com/watch?v=DuikFLPt8WQ)
- [Common Child HackerRank Solution](https://www.youtube.com/watch?v=ItRZRx8kvwY)
