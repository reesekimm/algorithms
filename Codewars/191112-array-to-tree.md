### 5kyu / Javascript

# [Fun with trees: array to tree](https://www.codewars.com/kata/fun-with-trees-array-to-tree/javascript)

## Challenge

You are given a non-null array of integers. Implement the method arrayToTree which creates a binary tree from its values in accordance to their order, while creating nodes by depth from left to right.

For example, given the array `[17, 0, -4, 3, 15]` you should create the following tree:

```
    17
   /  \
  0   -4
 / \
3   15
```

```
{
  "value": 17,
  "left": {
    "value": 0,
    "left": {
      "value": 3
    },
    "right": {
      "value": 15
    }
  },
  "right": {
    "value": -4
  }
}
```

The class TreeNode is available for you:

```js
var TreeNode = function(value, left, right) {
  this.value = value;
  this.left = left;
  this.right = right;
};
```

<br/>

## 문제 이해

배열을 인자로 받아서 이진 트리를 만드는 문제이다.

트리를 만들때는 상위 depth의 왼쪽 노드부터 차례대로 채워나간다.

<br/>

## 문제 풀이

임의의 배열을 트리로 바꿀때 어떤 규칙을 가지고 트리가 만들어지는지 찾아보았다.

```
[17, 0, -4, 3, 15, 8, 10, 1, 3, 9, 22]
```

일단 위 배열을 이진 트리로 만들면 다음과 같다.

```
        17
      /    \
     0      -4
   /   \    / \
  3    15  8   10
 / \   / \
1   2 3   9
```

그리고 각각의 노드별로 left 노드/right 노드의 관계를 파악해보았다. 이때 배열에서의 인덱스를 활용했다. (아래 표에서는 `i`로 표기)

|         노드         |  left 노드  |  right 노드  |
| :------------------: | :---------: | :----------: |
| **17** 　**`i = 0`** | 0 　`i = 1` | -4 　`i = 2` |
| **0** 　**`i = 1`**  | 3 　`i = 3` | 15 　`i = 4` |
| **-4** 　**`i = 2`** | 8 　`i = 5` | 10 　`i = 6` |
| **3** 　**`i = 3`**  | 1 　`i = 7` | 2 　`i = 8`  |
| **15** 　**`i = 4`** | 3 　`i = 9` | 9 　`i = 10` |

**노드가 하나씩 생성될 때마다 left 노드/right 노드의 인덱스가 규칙적으로 변한다는 사실**을 알 수 있다. 그리고 관계를 다시 정리해보면 다음과 같이 표현할 수 있다.

| 노드 |  left 노드  | right 노드  |
| :--: | :---------: | :---------: |
| `i`  | `i * 2 + 1` | `i * 2 + 2` |

트리가 생성되는 규칙을 파악했으니 이제 트리의 구조를 만들 방법을 생각해볼 차례다.

하나의 규칙을 가지고 동일한 작업을 반복해서 nested object를 만들어야 하기 때문에 재귀를 활용해보기로 했다.

<br/>

## 코드 구현

```js
function arrayToTree(array, i = 0) {
  if (array.length !== 0 && i < array.length) {
    return new TreeNode(
      array[i],
      arrayToTree(array, i * 2 + 1),
      arrayToTree(array, i * 2 + 2)
    );
  }
}
```

- 각 노드의 인덱스(`i`)를 함수의 인자로 추가하고 초기값을 0으로 할당해서 `root(= array[0])`노드부터 생성해간다.
- left 노드와 right 노드를 생성할때 재귀 호출을 하는데, 이때 인덱스(`i`)를 업데이트하여 인자로 전달한다.

<br/>

## 다른 풀이

<br/>

#### 1.

```js
function arrayToTree(array) {
  return (function nodeFromIndex(i) {
    if (array[i] === undefined) return;
    return new TreeNode(
      array[i],
      nodeFromIndex(i * 2 + 1),
      nodeFromIndex(i * 2 + 2)
    );
  })(0);
}
```

- 트리를 만드는 역할을 하는 별도의 함수를 리턴하면서 동시에 호출했다.

<br/>

#### 2.

```js
function arrayToTree(a) {
  a = a.map(x => new TreeNode(x));
  a.forEach((x, i) => ((x.left = a[2 * i + 1]), (x.right = a[2 * i + 2])));
  return a[0];
}
```

- 일단 `map`을 사용해서 배열을 이루는 각각의 요소들을 노드로 변환한 새로운 배열을 만든다.
- 노드로 이루어진 배열에 `forEach`로 loop을 돌면서 left 노드와 right 노드를 연결해주고 연결이 완료되면 배열의 첫번째 값을 리턴한다.
- callback 함수를 십분 활용한 참신한 풀이이다. 나중에 활용해봐야지!
