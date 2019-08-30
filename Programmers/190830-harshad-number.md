### lv.1 / Javascript

# [하샤드 수](https://programmers.co.kr/learn/courses/30/lessons/12947)

## 문제

양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

<br />

#### 제한 조건

- x는 1 이상, 10000 이하인 정수입니다.

<br />

#### 입출력 예

|              s                 |              return              |
| :----------------------------: | :------------------------------: |
|               10               |               true               |
|               12               |               true               |
|               11               |               false              |
|               13               |               false              |

<br />

#### 입출력 예 설명

입출력 예 #1  
10의 모든 자릿수의 합은 1입니다. 10은 1로 나누어 떨어지므로 10은 하샤드 수입니다.

입출력 예 #2  
12의 모든 자릿수의 합은 3입니다. 12는 3으로 나누어 떨어지므로 12는 하샤드 수입니다.

입출력 예 #3  
11의 모든 자릿수의 합은 2입니다. 11은 2로 나누어 떨어지지 않으므로 11는 하샤드 수가 아닙니다.

입출력 예 #4  
13의 모든 자릿수의 합은 4입니다. 13은 4로 나누어 떨어지지 않으므로 13은 하샤드 수가 아닙니다.

<br />

## 코드 구현

```javascript
function solution(x) {
    var sumOfNums = (x + "").split("").reduce((sum, str) => sum + (+str), 0);
    return x % sumOfNums ? false : true;
}
```

<br />

## 다른 풀이

### Solution 1

```javascript
function solution(x) {
    return !(x % ((x + "").split("").reduce((sum, str) => +sum + +str)));
}
```
- `reduce` 사용 시 초기값을 할당하지 않고 accumulator부터 바로 숫자로 변환했다 --- `+sum`
- `!`연산자를 한 번만 써서 0(falsy)을 true로, 그 외(truthy)는 false를 리턴하도록 처리했다.

<br />

### Solution 2
```javascript
function solution(x, i = 0, sum = 0) {
    return String(x).length == i ? x % sum == 0 : solution(x, i + 1, sum + String(x)[i] * 1);
}
```
- 인덱스`i`와 자릿수의 합 `sum`을 함수의 default parameter로 넣고
- 조건문의 false 표현식 위치에 재귀를 넣어서 각각의 자릿수를 더해준 뒤,
- 모든 자릿수를 전부 합했을 때 true 표현식이 실행되면서 나머지를 구한 결과를 리턴한다.

이런식으로 재귀를 활용해서 합을 구할 수도 있다:)
