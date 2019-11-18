### 6kyu / Javascript

# [Fun with trees: max sum](https://www.codewars.com/kata/fun-with-trees-max-sum/javascript)

## Challenge

You are given a binary tree. Implement the method maxSum which returns the maximal sum of a route from root to leaf. For example, given the following tree:

```
    17
   /  \
  3   -10
 /    /  \
2    16   1
         /
        13
```

The method should return **23**, since `[17,-10,16]` is the route from root to leaf with the maximal sum.

The class TreeNode is available for you:

```js
var TreeNode = function(value, left, right) {
  this.value = value;
  this.left = left;
  this.right = right;
};
```

<br />

## 문제 이해

1. 이진트리 객체를 인자로 받는다.
2. 트리의 root에서 하나의 leaf까지 이동할때 해당 경로상에 포함된 노드의 값들을 전부 더한 합계를 구한다.
3. 각각의 leaf에 대해 2번 과정을 반복한다.
4. 트리에서 나올 수 있는 가장 큰 합계를 반환한다.

```
    17
   /  \
  3   -10
 /    /  \
2    16   1
         /
        13
```

문제에 제시된 트리의 경우 2, 16, 13 총 3개의 leaf가 있고 root부터 leaf까지의 노드들의 합을 구하면 다음과 같다.

- 17 + 3 + 2 = 22
- 17 + (-10) + 16 = **23**
- 17 + (-10) + 1 + 13 = 21

이중에서 가장 큰 값은 23이다.

> 만약 root가 없을 경우 `0`을 반환하면 된다.

<br />

## 코드 구현

```js
function maxSum(root) {
  if (!root) return 0;

  let sums = [];

  function getSum(root, sum = root.value) {
    const { left, right } = root;

    if (!left && !right) {
      sums.push(sum);
      return;
    }

    if (left) {
      getSum(left, sum + left.value);
    }

    if (right) {
      getSum(right, sum + right.value);
    }
  }

  getSum(root, root.value);

  return Math.max(...sums);
}
```

다음과 같이 방향을 잡고 문제에 접근했다.

1. 각각의 leaf에 대해 root ~ leaf 경로상의 노드들의 합계를 구한다.
2. 이들 합계들 중에 최대값을 찾는다.

나는 임의의 배열 하나를 만들고 내부함수의 재귀를 통해 leaf별로 구한 합계를 배열에 push하도록 했다. 모든 leaf에 대해 합계를 구하는 과정이 끝나면 배열 내에서 가장 큰 값을 찾아서 리턴한다.

<br />

## 다른 풀이

<br />

#### 1.

```js
function maxSum(root) {
  if (!root) return 0;
  return root.value + Math.max(maxSum(root.left), maxSum(root.right));
}
```

- `maxSum`은 `(root 노드) + (left 노드와 right 노드 중 더 큰 값)`을 리턴하는 함수이다. 리턴 구문의 **`Math.max()` 내부에서 재귀 호출**을 하기 때문에 재귀가 완료되면 최종적으로는 가장 큰 값을 리턴하게 된다.

> 1.1 동일한 풀이 방법의 ES6 버전이다. 화살표 함수와 삼항 연산자를 써서 코드가 조금 더 간결해졌다.

```js
maxSum = root =>
  !root ? 0 : root.value + Math.max(maxSum(root.left), maxSum(root.right));
```

<br />

#### 2.

```js
function maxSum(root) {
  if (!root) return 0;
  let left = root.value + maxSum(root.left);
  let right = root.value + maxSum(root.right);
  return left > right ? left : right;
}
```

- root 노드의 left 노드와 right 노드에 대해 재귀를 돌면서 합계를 구하고 값을 비교해서 최종적으로 최대값이 리턴되도록 한다.
