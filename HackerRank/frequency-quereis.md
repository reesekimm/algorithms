# [Frequency Queries](https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps)

> Medium

<br />

## 문제 이해

```
[[operation, data], [operation, data], ...]
e.g. [[1, 3], [3, 17], [2, 2], [3, 11], ...]
```

위와 같이 구성된 이중배열 `queries`를 인자로 받아서 operation에 맞게 data를 처리한 뒤 3번 operation의 결과값이 담긴 배열을 반환하는 문제이다.

<br />

## 코드 구현 & 풀이 학습

```js
function freqQuery(queries) {
  const ds = new Map();
  const result = [];

  const ops = {
    1: (data) => {
      const value = ds.get(data); // O(n) (worst)
      ds.set(data, value ? value + 1 : 1);
    },
    2: (data) => {
      const value = ds.get(data); // O(n) (worst)
      if (value) {
        ds.set(data, value - 1);
      }
    },
    3: (freq) => result.push([...ds.values()].some((data) => data === freq) ? 1 : 0), // O(n^2) (worst)
  };

  queries.forEach(([op, data]) => ops[op](data)); // O(n)

  return result;
}
```

1, 2, 3 operation 처리 로직을 `ops` 객체에 명시해두고 `queries` 인자를 순회하면서 요청을 처리해주었다.
11번 testcase에서 계속해서 시간초과로 인한 fail이 뜨는 바람에 성능을 개선해주는 방법을 고민해야 했다.

<br />

성능을 개선하기 위해 수정한 부분을 정리해보면 다음과 같다.

1. **데이터 캐싱**

   before

   ```js
   ds.set(data, ds.get(data) ? ds.get(data) + 1, 1);
   ```

   after

   ```js
   const value = ds.get(data);
   ds.set(data, value ? value + 1 : 1);
   ```

   빈번하게 사용되는 값을 변수에 담아놓고 재사용 한다. 겨우 2번밖에 안쓰이는데 캐싱이 굳이 필요할까 싶지만 처리할 데이터의 갯수가 많아질수록 성능을 저하하는 요인이 될 수 있다.

<br />

2. **삼항연산자 대신 if문을 사용해서 필요한 처리만 해주기**

   before

   ```js
   ds.set(data, value ? value - 1 : 0);
   ```

   after

   ```js
   if (value) {
     ds.set(data, value - 1);
   }
   ```

   2번 operation의 경우 찾는 값이 있는 경우에만 1을 빼주면 된다. 불필요하게 삼항연산자를 사용해서 0을 할당해줄 필요가 없다.

<br />

사소한 처리 같지만 데이터의 양이 많아질수록 그 영향력이 커진다는걸 배웠다.

<br />

다음과 같이 `queries`를 순회하면서 switch문을 사용할 수도 있다.

```js
function freqQuery(queries) {
  let map = new Map();
  let result = [];

  queries.forEach(([type, val]) => {
    const mVal = map.get(val);
    switch (type) {
      case 1:
        mVal ? map.set(val, mVal + 1) : map.set(val, 1);
        break;
      case 2:
        if (mVal) map.set(val, mVal - 1);
        break;
      case 3:
        result.push([...map.values()].some((v) => v === val) ? 1 : 0);
        break;
      default:
        break;
    }
  });

  return result;
}
```
