### 5kyu / Javascript

# [Double Cola](https://www.codewars.com/kata/double-cola/javascript)

## 문제

Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine; there are no other people in the queue. The first one in the queue (Sheldon) buys a can, drinks it and doubles! The resulting two Sheldons go to the end of the queue. Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on.

For example, Penny drinks the third can of cola and the queue will look like this:

```
Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny
```

Write a program that will return the name of the person who will drink the n-th cola.

<br />

#### Input

The input data consist of an array which contains at least 1 name, and single integer n which may go as high as the biggest number your language of choice supports (if there's such limit, of course).

<br />

#### Output / Examples

Return the single line — the name of the person who drinks the n-th can of cola. The cans are numbered starting from 1.

```
whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1) == "Sheldon"
whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52) == "Penny"
whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951) == "Leonard"
```

<br />

## 문제 이해

'Double Cola'라는 콜라 자판기 앞에 Sheldon, Leonard, Penny, Rajesh 그리고 Howard가 줄을 서있다. 먼저, 맨 앞에 서있던 Sheldon이 콜라를 뽑아서 마셨더니 Sheldon이 2명이 되었다. 그리고 2명의 Sheldon은 다시 맨 뒤로 가서 줄을 선다.  
그 다음 Leonard가 콜라를 뽑아서 마셨더니 Leonard 역시 2명으로 뻥튀기(?)되었고, 역시 맨 뒤로 가서 Sheldon의 뒤에 줄을 선다.  
그 다음 3번째로 줄을 서있던 Penny가 콜라를 마시게 되면 줄은 다음과 같아 진다.

```
Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny
```

이런식으로 콜라를 마시면 사람이 뻥튀기되는 상황이 무한 반복 된다. 이제 우리는 _n번째 콜라를 마시는 사람이 누군지_ 찾는 함수 `whoIsNext()`를 작성하게된다.

1. 함수는 최소한 1명의 이름을 담은 배열과, 정수 n을 인자로 받는다.

2. 함수는 n번째 콜라를 마시는 사람의 이름을 리턴해주면 된다. (콜라의 갯수는 1부터 센다.)

<br />

## 문제 해결 방향

맨 처음 3명이 줄을 서 있었다고 가정해보고,  
doubled 됨에 따라 줄이 변하는 모습을 누적해서 써보면..

```
* 사람 수 = 3 (default)

["a", "b", "c"]
-> 전체 : 2^0 * 3

["a", "b", "c" / "a", "a", "b", "b", "c", "c"]
-> 전체 : (2^0 * 3) + (2^1 * 3)

["a", "b", "c" / "a", "a", "b", "b", "c", "c" / "a", "a", "a", "a", "b", "b", "b", "b", "c", "c", "c", "c"]
-> 전체 : (2^0 * 3) + (2^1 * 3) + (2^2 * 3)

...

```

복제된 사람이 2<sup>0</sup>, 2<sup>1</sup>, 2<sup>2</sup>, ... 이런식으로 증가한다는 사실을 알 수 있고, 전체 줄의 길이는 다음과 같다.

```
(2<sup>0</sup> + 2<sup>1</sup> + 2<sup>2</sup> + 2<sup>3</sup> + ... ) * default 사람 수
```

이제 n이 어디에 위치하는지 파악해야하는데,  
만약 n이 2<sup>k</sup>인 구간에 있다면  
맨 앞부터 2<sup>k - 1</sup>까지의 구간을 제거해주고,  
나머지를 2<sup>k</sup>(=복제된 사람 수)로 나눠서  
n번째 사람이 누구인지 찾을 수 있다.

> 참고로 `2^0 + 2^1 + 2^2 + 2^3 + ...`를 계산하기 위해 등비급수 공식을 활용했다.
> ![2019-08-16 15;24;38](https://user-images.githubusercontent.com/42695954/63147797-36b55380-c03a-11e9-8f0d-3b71c6ed741c.PNG)

<br />

## 코드 구현

```javascript
function whoIsNext(names, r) {
  var numOfNames = names.length;
  if (numOfNames === 1) return names[0];

  var i = 0;
  while ((Math.pow(2, i + 1) - 1) * numOfNames < r) {
    i++;
  }

  var doMath = Math.pow(2, i);
  var remove = (r - (doMath - 1) * numOfNames) / doMath;
  var getName = Math.ceil(remove);

  return names[getName - 1];
}
```

<br />

## 다른 방법

```javascript
function whoIsNext(names, r) {
  var peopleInLine = names.length;
  var copiesOfEachPerson = 1;

  while (r > peopleInLine) {
    r -= peopleInLine;
    copiesOfEachPerson *= 2;
    peopleInLine *= 2;
  }

  return names[Math.floor((r - 1) / copiesOfEachPerson) % peopleInLine];
}
```

- 변수명을 직관적으로 써서 코드를 이해하기가 쉬웠다.
- while문을 돌면서 2<sup>k</sup> 구간별로 변수들의 값을 제어해주는 방법을 나중에 써보고 싶다는 생각이 들었다.

<br />

## 기타 배운점 / 느낀점

for문이나 if문은 조건문을 쓰는게 수월해졌는데 while문은 조건문을 쓰는 연습이 더 필요한 것 같다. 오늘 문제를 푸는데 초반에 while문 조건을 잘못 써서 loop를 아예 돌지 않는 상황이 발생했었기 때문에..  
앞으로 loop를 쓸 일이 있을 때 상황에 맞게 for문 대신 while문을 써보면서 의식적으로 훈련해봐야겠다.
