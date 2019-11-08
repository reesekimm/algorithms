### 6kyu / Javascript

# [Sum The Tree](https://www.codewars.com/kata/sum-the-tree/javascript)

## Challenge

Given a node object representing a binary tree:

```
// Tree layout

10
| \
1  2


// Tree in Javascript code

{
  value: 10,
  left: {
    value: 1,
    left: null,
    right: null
  },
  right: {
    value: 2,
    left: null,
    right: null
  }
}

=> returns 13
```

write a function that returns the sum of all values, including the root. Absence of a node will be indicated with a null value.

<br/>

## 문제 이해

Binary Tree에 있는 모든 수들의 합을 구하는 문제이다.

<br/>

## 코드 구현

### 1차

```js
function sumTheTreeValues(node, total = node.value) {
  const { left, right } = node;

  if (left) {
    total += left.value;
    sumTheTreeValues(left, total);
  }

  if (right) {
    total += right.value;
    sumTheTreeValues(right, total);
  }

  return total;
}
```

`sumTheTreeValues`가 실행될 때 마다 변수 `total`을 업데이트 한다. 하지만 재귀에 의해 콜스택에 쌓여있던 `sumTheTreeValues`가 역순으로 실행되면서 결국 최종적으로 리턴하는 `total`값은 `root의 value + left.value + right.value`가 된다. 재귀가 아무 소용 없어지는 셈이다.<br/>
`total`의 최종 업데이트 값을 그대로 리턴하는 방법을 찾기위해 `update local variable in recursion javascript`라는 키워드로 검색을 해보았고 클로저를 활용하는 [방법](https://stackoverflow.com/questions/40017796/make-javascript-local-variable-to-global-for-recursive-loops)을 찾았다.

<br/>

### 2차

```js
function sumTheTreeValues(node, total = node.value) {
  const sum = node => {
    const { left, right } = node;

    if (left) {
      total += left.value;
      sum(left);
    }

    if (right) {
      total += right.value;
      sum(right);
    }
  };

  sum(node);

  return total;
}
```

내부함수 `sum`을 통해 local scope에 있는 `total`을 업데이트 해주었더니 최종적으로 업데이트된 `total`값이 리턴됐다.

<br/>

## 다른 풀이

### 1.

```js
function sumTheTreeValues(root) {
  return !root
    ? 0
    : root.value + sumTheTreeValues(root.left) + sumTheTreeValues(root.right);
}
```

- node가 존재할 경우 자기 자신의 value를 더해주는 재귀 함수를 계속해서 호출한다.
- ternary operator를 쓰고 재귀 호출하는 부분을 `+` 연산자로 연결해서 코드가 굉장히 간결해졌다.

<br/>

### 2.

```js
let sumTheTreeValues = (root, prev = 0) => {
  if (root.left) {
    prev = sumTheTreeValues(root.left, prev);
  }

  if (root.right) {
    prev = sumTheTreeValues(root.right, prev);
  }

  return (prev += root.value);
};
```

- `prev`라는 변수를 재귀함수의 인자로 전달하고 동시에 재귀함수의 리턴값을 가리키도록 업데이트 해나간다.

<br/>

## 기타 느낀점

- 재귀, 자료구조는 계속해서 연습해 봐야겠다.
- 자바스크립트 스코프와 클로저에 대해 정리하자.
