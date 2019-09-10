### 6kyu / Javascript

# [Persistent Bugger](https://www.codewars.com/kata/persistent-bugger/javascript)

## 문제

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

<br />

#### Input

```
 persistence(39) === 3 // because 3*9 = 27, 2*7 = 14, 1*4=4
                       // and 4 has only one digit

 persistence(999) === 4 // because 9*9*9 = 729, 7*2*9 = 126,
                        // 1*2*6 = 12, and finally 1*2 = 2

 persistence(4) === 0 // because 4 is already a one-digit number
```

<br />

## 문제 이해

숫자를 인자로 받아서 각 자릿수를 곱해준다.  
곱한 결과가 한 자릿수가 될 때 까지 곱한 횟수를 결과값으로 리턴해주면 된다.  
처음에 인자로 받은 숫자가 한 자릿수일 경우 0을 리턴한다.

<br />

## 코드 구현

```javascript
function persistence(num) {
  if (num < 10) return 0;

  var count = 0;
  while (num >= 10) {
    num = num
      .toString()
      .split("")
      .reduce((mul, digit) => mul * +digit);
    count++;
  }

  return count;
}
```

`+`연산자를 사용해서 문자열을 숫자로 바꾸는 방법을 이 문제를 풀 때 써볼 수 있어서 좋았다.  
알고리즘 풀 때 말고 웹/앱을 만들어 볼 때도 써보면 좋을듯!

<br />

## 다른 방법

```javascript
const persistence = num => {
  return `${num}`.length > 1
    ? 1 + persistence(`${num}`.split("").reduce((a, b) => a * +b))
    : 0;
};
```

간결하면서도 멋진 코드다ㅠㅠ!

- 숫자를 문자열로 변환하는 별도의 과정 없이 Template literal을 사용해서 숫자의 길이를 바로 체크했다.
- 숫자의 길이가 1보다 길면 (숫자가 10 이상이면), `1 + 재귀호출`로 카운팅과 동시에 곱셈연산을 해주고
- 숫자의 길이가 1보다 짧으면 (숫자가 10 미만이면), 0을 리턴해준다.
