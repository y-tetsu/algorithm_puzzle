# algorithm_puzzle
## 参考書籍
- 「アルゴリズムパズル プログラマのための数学パズル入門」 Anany Levitin、Maria Levitin著 黒川 洋、松崎 公紀訳 株式会社オライリー・ジャパン [ISBN978-4-87311-669-3](https://www.oreilly.co.jp/books/9784873116693/)

## チュートリアル
### 1. Magic Square
```
$ py -3.7 t01_magic_square.py
(2, 7, 6)
(9, 5, 1)
(4, 3, 8)

(2, 9, 4)
(7, 5, 3)
(6, 1, 8)

(4, 3, 8)
(9, 5, 1)
(2, 7, 6)

(4, 9, 2)
(3, 5, 7)
(8, 1, 6)

(6, 1, 8)
(7, 5, 3)
(2, 9, 4)

(6, 7, 2)
(1, 5, 9)
(8, 3, 4)

(8, 1, 6)
(3, 5, 7)
(4, 9, 2)

(8, 3, 4)
(1, 5, 9)
(6, 7, 2)

count = 8
```

### 2. The n-Queens Problem
```
$ py -3.7 t02_the_n_queens_problem.py
['_', '_', 'Q', '_']
['Q', '_', '_', '_']
['_', '_', '_', 'Q']
['_', 'Q', '_', '_']

['_', 'Q', '_', '_']
['_', '_', '_', 'Q']
['Q', '_', '_', '_']
['_', '_', 'Q', '_']

(N=4) count = 2

['Q', '_', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', 'Q', '_']
['_', '_', '_', '_', 'Q', '_', '_', '_']
['_', '_', '_', '_', '_', '_', '_', 'Q']
['_', 'Q', '_', '_', '_', '_', '_', '_']
['_', '_', '_', 'Q', '_', '_', '_', '_']
['_', '_', '_', '_', '_', 'Q', '_', '_']
['_', '_', 'Q', '_', '_', '_', '_', '_']

['Q', '_', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', 'Q', '_']
['_', '_', '_', 'Q', '_', '_', '_', '_']
['_', '_', '_', '_', '_', 'Q', '_', '_']
['_', '_', '_', '_', '_', '_', '_', 'Q']
['_', 'Q', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', 'Q', '_', '_', '_']
['_', '_', 'Q', '_', '_', '_', '_', '_']
                   :
                   :
                   :
['_', '_', 'Q', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', 'Q', '_', '_']
['_', '_', '_', 'Q', '_', '_', '_', '_']
['_', 'Q', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', '_', 'Q']
['_', '_', '_', '_', 'Q', '_', '_', '_']
['_', '_', '_', '_', '_', '_', 'Q', '_']
['Q', '_', '_', '_', '_', '_', '_', '_']

(N=8) count = 92
```

### 3. Celebrity Problem
```
$ py -3.7 t03_celebrity_problem.py
celebrity = 7

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 3, 4, 5, 6, 7, 8, 9]
[0, 4, 5, 6, 7, 8, 9]
[0, 5, 6, 7, 8, 9]
[0, 6, 7, 8, 9]
[0, 7, 8, 9]
[7, 8, 9]
[7, 9]
[7]

result = 7
```

### 4. Number Guessing
```
$ py -3.7 t04_number_guessing.py
n = 10 number = 8

( 1) Is the correct answer greater than 5 ? True
( 2) Is the correct answer greater than 8 ? False
( 3) Is the correct answer greater than 7 ? True

result = 8

n = 1000000 number = 367506

( 1) Is the correct answer greater than 500000 ? False
( 2) Is the correct answer greater than 250000 ? True
( 3) Is the correct answer greater than 375000 ? False
( 4) Is the correct answer greater than 312500 ? True
( 5) Is the correct answer greater than 343750 ? True
( 6) Is the correct answer greater than 359375 ? True
( 7) Is the correct answer greater than 367188 ? True
( 8) Is the correct answer greater than 371094 ? False
( 9) Is the correct answer greater than 369141 ? False
(10) Is the correct answer greater than 368165 ? False
(11) Is the correct answer greater than 367677 ? False
(12) Is the correct answer greater than 367433 ? True
(13) Is the correct answer greater than 367555 ? False
(14) Is the correct answer greater than 367494 ? True
(15) Is the correct answer greater than 367525 ? False
(16) Is the correct answer greater than 367510 ? False
(17) Is the correct answer greater than 367502 ? True
(18) Is the correct answer greater than 367506 ? False
(19) Is the correct answer greater than 367504 ? True
(20) Is the correct answer greater than 367505 ? True

result = 367506
```

### 5. Tromino Puzzle
```
$ py -3.7 t05_tromino_puzzle.py
(Initial)
[-1, -1, -1, -1, -1, -1, -1, -1]
[-1, -1, -1, -1, -1, -1, -1, -1]
[-1, -1, -1, -1, -1, -1, -1, -1]
[-1, -1, -1, -1, -1, 10, -1, -1]
[-1, -1, -1, -1, -1, -1, -1, -1]
[-1, -1, -1, -1, -1, -1, -1, -1]
[-1, -1, -1, -1, -1, -1, -1, -1]
[-1, -1, -1, -1, -1, -1, -1, -1]

(Result)
[13, 13, 14, 14, 18, 18, 19, 19]
[13, 12, 12, 14, 18, 17, 17, 19]
[15, 12, 16, 16, 20, 20, 17, 21]
[15, 15, 16, 11, 20, 10, 21, 21]
[23, 23, 24, 11, 11, 28, 29, 29]
[23, 22, 24, 24, 28, 28, 27, 29]
[25, 22, 22, 26, 30, 27, 27, 31]
[25, 25, 26, 26, 30, 30, 31, 31]
```
