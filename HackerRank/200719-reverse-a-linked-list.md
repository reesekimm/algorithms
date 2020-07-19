# [Reverse a linked list](https://www.hackerrank.com/challenges/reverse-a-linked-list/problem)

> Easy

<br />

## 문제 이해

단일 연결 리스트를 역순으로 뒤집어서 reverse된 연결 리스트를 만드는 문제

<br />

## 코드 구현 & 풀이 학습

1.

```js
function Node(data) {
  return {
    data,
    next: null,
  };
}

function reverse(head) {
  const nodes = [];
  while (head.next) {
    // O(n)
    nodes.push(new Node(head.data));
    head = head.next;
  }
  nodes.push(new Node(head.data)); // O(1)

  const lastIdx = nodes.length - 1;
  for (let i = lastIdx; i > 0; i--) {
    // O(n)
    nodes[i].next = nodes[i - 1];
  }

  return nodes[lastIdx];
}

// Time Complexity: O(n)
// Place Complexity: O(n)
```

1. 임의의 빈 배열을 하나 생성해 놓고 리스트를 순회하면서 head 부터 tail까지 각각의 노드가 가지고 있는 data를 새로운 노드로 만들어 배열에 추가했다.
2. 배열을 역순으로 순회하면서 배열 안의 노드를 연결하고 for문 순회가 종료되면 배열의 마지막 요소에 인덱스로 접근해서 완성된 리스트를 얻었다.

2번이 가능한 이유는 노드가 data와 next 프로퍼티를 갖는 '객체'이며 노드를 연결할때 해당 노드가 위치한 '메모리 주소'를 공유하게끔 만들어주었기 때문이다.  
다시 말해 for문 안에서 `nodes[i].next = nodes[i - 1];` 이 구문이 하는 역할은 인덱스 `i`에 위치한 노드의 next 프로퍼티 변수가 인덱스 `i - 1`에 위치한 노드의 메모리 공간을 참조하도록(가리키도록) 만든 것이다.

<br />

2. (풀이 학습)

```js
function reverse(head) {
  var curr = head;
  var prevNode = null;
  var nextNode = null;

  while (curr !== null) {
    // O(n)
    nextNode = curr.next;
    curr.next = prevNode;
    prevNode = curr;
    curr = nextNode;
  }

  return prevNode;
}

// Time Complexity: O(n)
// Place Complexity: O(1)
```

포인터를 잘 활용하니 시간 복잡도와 공간 복잡도가 모두 개선되었다.  
포인터가 익숙하지 않다보니 혼란스럽다. [Geeks for Geeks - Reverse a linked list](https://www.geeksforgeeks.org/reverse-a-linked-list/)를 참고해보니 각 노드의 next 포인터가 가리키는 방향을 뒤집어주는게 관건이었다. 그리고 뒤집기 전에 next 포인터가 가리키던 노드를 nextNode라는 변수에 저장해주어야 한다.
