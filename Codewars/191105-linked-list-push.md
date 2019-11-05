### 7kyu / Javascript

# [Linked Lists - Push & BuildOneTwoThree](https://www.codewars.com/kata/55be95786abade3c71000079)

## Challenge

Write `push()` and `buildOneTwoThree()` functions to easily update and initialize linked lists. Try to use the `push()` function within your `buildOneTwoThree()` function.

Here's an example of `push()` usage:

```
var chained = null
chained = push(chained, 3)
chained = push(chained, 2)
chained = push(chained, 1)
push(chained, 8) === 8 -> 1 -> 2 -> 3 -> null
```

The `push()` function accepts head and data parameters, where head is either a node object or null/None/nil. Your push implementation should be able to create a new linked list/node when head is null/None/nil.

The buildOneTwoThree function should create and return a linked list with three nodes: `1 -> 2 -> 3 -> null`

<br />

## 문제 이해

`push()`, `buildOneTwoThree()` 두 개의 함수를 작성하는 문제이다.

- `push(head, data)`: 기존 연결 리스트의 head에 data 노드를 연결하여 새로운 연결리스트를 생성한다. (head는 노드 또는 `null`)
- `buildOneTwoThree`: `1 -> 2 -> 3 -> null` 3개의 노드를 가지는 연결 리스트를 생성한다.

> `buildOneTwoThree()`를 작성할 때 `push()`를 활용해본다.

<br />

## 코드 구현

```js
function Node(data) {
  this.data = data;
  this.next = null;
}

function push(head, data) {
  let newNode = new Node(data);
  if (head) {
    newNode.next = head;
  }
  return newNode;
}

function buildOneTwoThree() {
  return push(push(new Node(3), 2), 1);
}
```

<br />

## 다른 풀이 분석

### 1.

```js
function push(head, data) {
  return new Node(data, head);
}

function buildOneTwoThree() {
  return [3, 2, 1].reduce((head, data) => push(head, data), null);
}

function Node(data, next = null) {
  this.data = data;
  this.next = next;
}
```

- `buildOneTwoThree`를 구현할때 `reduce`를 쓰고 `reduce`의 callback 함수가 `push`함수를 리턴하는 방식을 썼다. 함수형 프로그래밍을 잘 활용한 것 같다.

<br />

### 2.

```js
var push = (head, data) => new Node(data, head);

var build = (...args) => args.reduce(push, null);

var buildOneTwoThree = build.bind(null, 3, 2, 1);

var Node = (data, next = null) => ({ data, next });
```

- 함수형 프로그래밍과 ES6를 적재적소에 사용한 점이 돋보이는 풀이다.
- `build`라는 별도의 함수에 `bind`메서드를 사용하여 data를 `arguments`로 전달하면서 새로운 함수를 만들고 그 함수를 `buildOneTwoThree` 변수에 할당하는 식으로 `buildOneTwoThree` 함수를 구현했다.
- `build` 함수의 파라미터 위치에 rest parameter를 사용해서 전달받은 `arguments`를 배열로 나타낼수 있게 했다.
