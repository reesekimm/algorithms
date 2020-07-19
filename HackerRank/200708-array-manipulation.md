# [Array Manipulation](https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays)

> Hard

## 문제 이해

길이가 `n`이고 0으로 채워진 배열내의 값들에 `queries`에 명시된 규칙대로 일정한 값을 계속해서 더해준 뒤, 배열 내에서 가장 큰 값을 구하는 문제이다.  
`queries`는 이차원 배열이며, 다음과 같이 `[a, b, k]`로 구성되어 있다.

```
[[1, 5, 3], [4, 8, 7], [6, 9, 1]]
```

`a`, `b`는 배열 내 인덱스를 의미하는데, 실제 배열의 인덱스보다 1 크다.

```
index->	 1 2 3  4  5 6 7 8 9 10
        [0,0,0, 0, 0,0,0,0,0, 0]
        [3,3,3, 3, 3,0,0,0,0, 0]
        [3,3,3,10,10,7,7,7,0, 0]
        [3,3,3,10,10,8,8,8,1, 0]
```

`k`는 각각의 인덱스 범위에 더해줄 값이다. 예를들어 `[1, 5, 3]`은 인덱스 1부터 5까지의 요소에 3씩 더해주라는 의미이다.  
최종적으로는 모든 `queries`대로 값을 더해준한 뒤 배열 내에서 가장 큰 값을 반환하면 된다.

<br />

## 코드 구현

1차

```js
function arrayManipulation(n, queries) {
  const arr = Array(n).fill(0);
  queries.forEach(([a, b, k]) => {
    for (let i = a - 1; i < b; i++) {
      arr[i] += k;
    }
  });
  return Math.max(...arr);
}
```

가장 먼저 떠오른 직관적인 풀이이다.  
0으로 채워진 길이가 `n`인 배열을 생성한 뒤 `queries`배열을 순회하며 명시된 값을 계속해서 더해준다.  
시간복잡도는 `O(n * m)`이고, 시간초과로 인해 일부 테스트 케이스를 통과하지 못했다.

<br />

2차 (풀이 학습)

```js
function arrayManipulation(n, queries) {
  const arr = Array(n + 1).fill(0);

  // create prefix sum array
  for (var i = 0, numOfQueries = queries.length; i < numOfQueries; i++) {
    arr[queries[i][0] - 1] += queries[i][2];
    arr[queries[i][1]] -= queries[i][2];
  }

  let max = 0;
  let temp_max = 0;

  // scan the prefix sum array, and then return the max sum
  for (var i = 0; i < arr.length; i++) {
    temp_max += arr[i];
    max = Math.max(max, temp_max);
  }

  return max;
}
```

prefix sum algorithm을 사용한 풀이 방법이다.

> prefix sum algorithm이란, x0, x1 … xn까지의 수가 있을 때 연속된 수들의 합을 다음과 같이 나타내고
>
> ```
> y0 = x0
> y1 = x0 + x1
> y2 = x0 + x1 + x2
> ...
> ```
>
> 특정 범위의 부분합을 구할 때 미리 계산해놓은 합(prefix sum)을 사용하는 알고리즘을 말한다.
>
> ```
> S[j] - S[i - 1] = a[i] + a[i + 1] + ... + a[j - 1] + a[j]
> ```

![solve the problem using prefix sum](https://i.postimg.cc/s23wRmY9/image.png)

queries를 처리할때 순회를 돌면서 indice 범위 내의 모든 값들을 더해주는 작업을 하는 대신, `a`, `b + 1`에만 값을 더해주기 때문에 시간복잡도가 `O(n + m)`이 되면서 성능이 개선되었다.

<br />

`a` 대신 `a -1`을, `b + 1` 대신 `b`를 사용하고, for문 대신 reduce를 사용하면 코드가 좀 더 깔끔해진다.

```js
function arrayManipulation(n, queries) {
  const arr = new Array(n).fill(0);
  let result = 0;

  queries.forEach(([a, b, k]) => {
    arr[a - 1] += k;
    if (b < arr.length) {
      arr[b] -= k;
    }
  });

  arr.reduce((a, b) => {
    const acc = a + b;
    result = Math.max(result, acc);
    return acc;
  }, 0);

  return result;
}
```

<br />

---

- [prefix sum - wikipedia](https://en.wikipedia.org/wiki/Prefix_sum)
- [누적 합(Prefix sum)을 이용한 구간 합 구하기 기본 문제](https://twpower.github.io/157-prefix-sum-basic-problem)
- [prefix sum algorithm](https://www.youtube.com/watch?v=pVS3yhlzrlQ&t=49s)
- [Array Manipulation Hackerrank Solution](https://www.youtube.com/watch?v=hDhf04AJIRs)
