### 5kyu / Javascript

# [Did I Finish my Sudoku?](codewars.com/kata/did-i-finish-my-sudoku/javascript)

## Challenge

Write a function done_or_not/DoneOrNot passing a board(`list[list_lines]`) as parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'

Sudoku rules:

Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.

Rows:

<img src="https://user-images.githubusercontent.com/42695954/68298866-cddff380-00dd-11ea-8ba8-cd304c52ec6b.png" width="300"/>

There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.

In the illustration the numbers 5, 3, 1, and 2 are the "givens". They can not be changed. The remaining numbers in black are the numbers that you fill in to complete the row.

Columns:

<img src="https://user-images.githubusercontent.com/42695954/68298904-dd5f3c80-00dd-11ea-9c01-070c907d93c4.png" width="50"/>

There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Again, there may not be any duplicate numbers in any column. Each column will be unique as a result.

In the illustration the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining numbers as shown in black to complete the column.

Regions:

<img src="https://user-images.githubusercontent.com/42695954/68298920-e94afe80-00dd-11ea-8160-7906f16bdcf3.png" width="100"/>

A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.

Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Duplicate numbers are not permitted in any region. Each region will differ from the other regions.

In the illustration the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers as shown in black to complete the region.

Valid board example:

<img src="https://user-images.githubusercontent.com/42695954/68298928-f36cfd00-00dd-11ea-995e-864a09e3d223.png" width="300"/>

<br />

## 문제 이해

sudoku rule에 따라 sudoku가 완성됐는지 확인하는 함수를 구현하는 문제이다.

> 참고 - [suduku](https://ko.wikipedia.org/wiki/%EC%8A%A4%EB%8F%84%EC%BF%A0)

<br />

## 코드 구현

```js
function doneOrNot(board) {
  const result = {
    finished: "Finished!",
    again: "Try again!"
  };

  const set = new Set();

  // check rows
  for (var i = 0; i < 9; i++) {
    board[i].forEach(num => set.add(num));
    if (set.size !== 9) {
      return result.again;
    }
  }

  // check columns
  for (var i = 0; i < 9; i++) {
    set.clear();
    for (var j = 0; j < 9; j++) {
      set.add(board[j][i]);
    }
    if (set.size !== 9) {
      return result.again;
    }
  }

  // check regions
  for (var i = 0; i < 9; i += 3) {
    for (var j = 0; j < 9; j += 3) {
      set.clear();
      for (var k = i; k < i + 3; k++) {
        for (var l = j; l < j + 3; l++) {
          set.add(board[k][l]);
        }
      }
      if (set.size !== 9) {
        return result.again;
      }
    }
  }

  return result.finished;
}
```

- row, column, region 각각의 타입별로 control flow를 작성하고 1부터 9까지 모든 숫자가 한 번씩 등장하는지 확인했다.
- `Set`이 중복 데이터를 허용하지 않는다는 특성을 이용, 숫자를 `Set`에 추가한 후 `Set`의 크기가 9인지 여부를 체크했다. `Set`의 크기가 9보다 작다면 한 번도 등장하지 않는 숫자가 있다는 의미이다.

<br />

## 다른 풀이 분석

### 1.

```js
function doneOrNot(rows) {
  var columns = [],
    blocks = [];

  for (var i = 0; i < 9; i++) {
    columns[i] = [];

    for (var j = 0; j < 9; j++) {
      var k = Math.floor(i / 3) + Math.floor(j / 3) * 3;
      blocks[k] = blocks[k] || [];

      blocks[k].push(rows[i][j]);
      columns[i].push(rows[j][i]);
    }
  }

  var is_valid_row = row =>
    row
      .slice(0)
      .sort((a, b) => a - b)
      .join("") === "123456789";

  var is_valid =
    rows.every(is_valid_row) &&
    columns.every(is_valid_row) &&
    blocks.every(is_valid_row);

  return is_valid ? "Finished!" : "Try again!";
}
```

- 인자로 받는 `board`가 row의 집합인 것을 활용해서 동일하게 two dimensional array 형태로 column과 block(region)의 집합을 만든다.
- `is_valid_row`라는 판별 함수를 사용해서 각각의 집합을 테스트한다.
- `is_valid_row`함수 내부에서는 배열을 정렬한 후 문자열로 변환하여 `"123456789"`와 비교했다. 참신한 방법이다!

<br />

### 2.

```js
function doneOrNot(board) {
  var set1Array = new Set(),
    set2Array = new Set(),
    set3Array = new Set();

  for (var i = 0; i < 9; i++) {
    for (var j = 0; j < 9; j++) {
      set1Array.add(board[i][j]);
      set2Array.add(board[j][i]);
      set3Array.add(
        board[(i % 3) * 3 + (j % 3)][Math.floor(i / 3) * 3 + Math.floor(j / 3)]
      );
    }
    if (set1Array.size !== 9 || set2Array.size !== 9 || set3Array.size !== 9)
      return "Try again!";
    set1Array.clear();
    set2Array.clear();
    set3Array.clear();
  }
  return "Finished!";
}
```

- 역시 첫번째 풀이와 마찬가지로 row, column, region 각각의 집합을 만든다. 차이점이라면 배열대신 `Set`을 사용했다는 것.
- `Set`의 크기가 9인지 확인한 후 clear해주는 것을 반복한다.
