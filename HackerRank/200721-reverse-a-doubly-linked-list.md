# [Reverse a doubly linked list](https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem)

>

<br />

## 문제 이해

이중 연결 리스트의 Node들을 역순으로 재배치하는 문제!

<br />

## 코드 구현 & 풀이 학습

```js
function reverse(head) {
  let curr = head;
  let nextNode = null;
  let prevNode = null;

  while (curr) {
    // store nextNode
    nextNode = curr.next;

    // reverse pointer direction
    curr.next = prevNode;
    curr.prev = nextNode;

    // 'prevNode' should point 'curr'
    prevNode = curr;

    // 'curr' should point 'curr.next'(=nextNode)
    curr = nextNode;
  }

  return prevNode;
}
```

이중 연결 리스트 역시 단일 연결 리스트와 동일하게 포인터를 사용해서 풀 수 있었다. `curr.prev= nextNode;` 코드 한 줄만 추가해서 prev 포인터가 가리키는 방향을 뒤집어주면 된다.

prev, next 포인터의 방향을 뒤집어주고 나서 `prevNode`와 `nextNode`를 업데이트 할 때, 반드시 `prevNode`를 먼저 업데이트 해주어야 한다. `nextNode`를 먼저 할 경우 `curr` 변수가 가리키는 값이 `nextNode`가 되면서 `prevNode`가 `nextNode`와 동일한 값을 가리키게 되면서 원하는 로직을 구현할 수 없게 된다.

이 문제를 통해 포인터를 사용한 풀이를 복습할 수 있어서 좋았다. 비슷한 유형의 다른 문제가 나왔을 때 막힘없이 코드를 작성할 수 있도록 반복해서 연습해봐야겠다.
