# algorithm_puzzle
## チュートリアル
### 1. Magic Square
```
$ python t01_magic_square.py
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
$ python t02_the_n_queens_problem.py
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
$ python t03_celebrity_problem.py
group     = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
celebrity = 7

0 knows 1 ? False [0, 2, 3, 4, 5, 6, 7, 8, 9]
0 knows 2 ? False [0, 3, 4, 5, 6, 7, 8, 9]
0 knows 3 ? False [0, 4, 5, 6, 7, 8, 9]
0 knows 4 ? False [0, 5, 6, 7, 8, 9]
0 knows 5 ? False [0, 6, 7, 8, 9]
0 knows 6 ? False [0, 7, 8, 9]
0 knows 7 ? True  [7, 8, 9]
7 knows 8 ? False [7, 9]
7 knows 9 ? False [7]

result = 7
```

### 4. Number Guessing
```
$ python t04_number_guessing.py
n = 10 number = 8

( 1) greater than 5 ? True
( 2) greater than 8 ? False
( 3) greater than 7 ? True

result = 8

n = 1000000 number = 591009

( 1) greater than 500000 ? True
( 2) greater than 750000 ? False
( 3) greater than 625000 ? False
( 4) greater than 562500 ? True
( 5) greater than 593750 ? False
( 6) greater than 578125 ? True
( 7) greater than 585938 ? True
( 8) greater than 589844 ? True
( 9) greater than 591797 ? False
(10) greater than 590821 ? True
(11) greater than 591309 ? False
(12) greater than 591065 ? False
(13) greater than 590943 ? True
(14) greater than 591004 ? True
(15) greater than 591035 ? False
(16) greater than 591020 ? False
(17) greater than 591012 ? False
(18) greater than 591008 ? True
(19) greater than 591010 ? False
(20) greater than 591009 ? False

result = 591009
```

### 5. Tromino Puzzle
```
$ python t05_tromino_puzzle.py
(Initial)
[-1, -1, -1, -1, -1, -1, -1, -1]
[-1, -1, -1, -1, -1, -1, -1, -1]
[-1, -1, -1, -1, -1, -1, -1, -1]
[-1, -1, -1, -1, -1, -1, -1, -1]
[-1, -1, -1, -1, -1, -1, -1, -1]
[-1, -1, -1, -1, -1, -1, -1, -1]
[-1, -1, -1, -1, -1, 10, -1, -1]
[-1, -1, -1, -1, -1, -1, -1, -1]

(Result)
[13, 13, 14, 14, 18, 18, 19, 19]
[13, 12, 12, 14, 18, 17, 17, 19]
[15, 12, 16, 16, 20, 20, 17, 21]
[15, 15, 16, 11, 11, 20, 21, 21]
[23, 23, 24, 11, 28, 28, 29, 29]
[23, 22, 24, 24, 28, 27, 27, 29]
[25, 22, 22, 26, 30, 10, 27, 31]
[25, 25, 26, 26, 30, 30, 31, 31]
```

### 6. Anagram Detection
```
$ python t06_anagram_detection.py
(wordbook)
eat
silent
admirer
vase
canoe
stressed
talent
dusty
monday
cat
bored
butterfly
live
ate
listen
tea
evil
desserts
dictionary
save
ocean
married
dynamo
robed
latent
study
indicatory
act
flutterby

(signature)  (word)
acdiinorty   dictionary
acdiinorty   indicatory
aceno        canoe
aceno        ocean
act          act
act          cat
adeimrr      admirer
adeimrr      married
admnoy       dynamo
admnoy       monday
aelntt       latent
aelntt       talent
aesv         save
aesv         vase
aet          ate
aet          eat
aet          tea
bdeor        bored
bdeor        robed
beflrttuy    butterfly
beflrttuy    flutterby
deerssst     desserts
deerssst     stressed
dstuy        dusty
dstuy        study
eilnst       listen
eilnst       silent
eilv         evil
eilv         live
```

### 7. Cash Envelopes
```
$ python t07_cash_envelopes.py
money     = 1000
envelopes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 489]

(   1) pattern = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] total =    1
(   2) pattern = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0] total =    2
(   3) pattern = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0] total =    3
                              :
                              :
                              :
( 488) pattern = [0, 0, 0, 1, 0, 1, 1, 1, 1, 0] total =  488
( 489) pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1] total =  489
( 490) pattern = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1] total =  490
                              :
                              :
                              :
( 998) pattern = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1] total =  998
( 999) pattern = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] total =  999
(1000) pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] total = 1000
```

### 8. Two Jealous Husbands
```
$ python t08_two_jealous_husbands.py
+------------------------+
| H1 H2 |<[][]>  |       |
| W1 W2 |        |       |
+------------------------+
crossing river   = 5
optimal solution = 4

W1W2 -> W1 -> H1H2 -> H1 -> H1W1
W1W2 -> W1 -> H1H2 -> W2 -> W1W2
H2W2 -> H2 -> H1H2 -> H1 -> H1W1
H2W2 -> H2 -> H1H2 -> W2 -> W1W2

+------------------------------+
| H1 H2 H3 |<[][]>  |          |
| W1 W2 W3 |        |          |
+------------------------------+
crossing river   = 11
optimal solution = 4

W2W3 -> W2 -> W1W2 -> W1 -> H2H3 -> H2W2 -> H1H2 -> W3 -> W2W3 -> H1 -> H1W1
W2W3 -> W2 -> W1W2 -> W1 -> H2H3 -> H2W2 -> H1H2 -> W3 -> W2W3 -> W2 -> W1W2
H3W3 -> H3 -> W1W2 -> W1 -> H2H3 -> H2W2 -> H1H2 -> W3 -> W2W3 -> H1 -> H1W1
H3W3 -> H3 -> W1W2 -> W1 -> H2H3 -> H2W2 -> H1H2 -> W3 -> W2W3 -> W2 -> W1W2

+--------------------------------+
| H1 H2 H3 |<[][][]>  |          |
| W1 W2 W3 |          |          |
+--------------------------------+
crossing river   = 5
optimal solution = 6

W2W3 -> W2 -> H1H2H3 -> W3 -> W1W2W3
W1W2W3 -> W1 -> H1H2H3 -> H1 -> H1W1
W1W2W3 -> W1 -> H1H2H3 -> W2 -> W1W2
W1W2W3 -> W1 -> H1H2H3 -> W2W3 -> W1W2W3
W1W2W3 -> W1W2 -> H1H2H3 -> W3 -> W1W2W3
H3W3 -> H3 -> H1H2H3 -> W3 -> W1W2W3
```

### 9. Guarini's Puzzle
```
$ python t09_guarini's_puzzle.py
0
-------
|B| |B|
-------
| | | |
-------
|W| |W|
-------

1
-------
| | |B|
-------
| | | |
-------
|W|B|W|
-------

2
-------
| | | |
-------
|B| | |
-------
|W|B|W|
-------

3
-------
| | |B|
-------
|B| | |
-------
|W| |W|
-------

4
-------
| |W|B|
-------
|B| | |
-------
|W| | |
-------

5
-------
| |W|B|
-------
| | | |
-------
|W| |B|
-------

6
-------
| |W| |
-------
|B| | |
-------
|W| |B|
-------

7
-------
| |W| |
-------
|B| |W|
-------
| | |B|
-------

8
-------
| | | |
-------
|B| |W|
-------
|W| |B|
-------

9
-------
| |B| |
-------
|B| |W|
-------
|W| | |
-------

10
-------
| |B| |
-------
| | |W|
-------
|W| |B|
-------

11
-------
|W|B| |
-------
| | | |
-------
|W| |B|
-------

12
-------
|W|B| |
-------
| | |W|
-------
| | |B|
-------

13
-------
|W| | |
-------
| | |W|
-------
|B| |B|
-------

14
-------
| | | |
-------
| | |W|
-------
|B|W|B|
-------

15
-------
|W| | |
-------
| | | |
-------
|B|W|B|
-------

16
-------
|W| |W|
-------
| | | |
-------
|B| |B|
-------

result = 16
```

### 10. Optimal Pie Cutting
```
$ python t10_optimal_pie_cutting.py
-----
n = 5

* check all patterns *
 - h = 0, v = 5, pie = (h + 1) * (v + 1) = 6
 - h = 1, v = 4, pie = (h + 1) * (v + 1) = 10
 - h = 2, v = 3, pie = (h + 1) * (v + 1) = 12
 - h = 3, v = 2, pie = (h + 1) * (v + 1) = 12
 - h = 4, v = 1, pie = (h + 1) * (v + 1) = 10
 - h = 5, v = 0, pie = (h + 1) * (v + 1) = 6
max_pie = 12

* solve a formula *
 - h = n // 2 = 2
 - v = n - h  = 3
max_pie = (h + 1) * (v + 1) = 12

-----
n = 10

* check all patterns *
 - h = 0, v = 10, pie = (h + 1) * (v + 1) = 11
 - h = 1, v = 9, pie = (h + 1) * (v + 1) = 20
 - h = 2, v = 8, pie = (h + 1) * (v + 1) = 27
 - h = 3, v = 7, pie = (h + 1) * (v + 1) = 32
 - h = 4, v = 6, pie = (h + 1) * (v + 1) = 35
 - h = 5, v = 5, pie = (h + 1) * (v + 1) = 36
 - h = 6, v = 4, pie = (h + 1) * (v + 1) = 35
 - h = 7, v = 3, pie = (h + 1) * (v + 1) = 32
 - h = 8, v = 2, pie = (h + 1) * (v + 1) = 27
 - h = 9, v = 1, pie = (h + 1) * (v + 1) = 20
 - h = 10, v = 0, pie = (h + 1) * (v + 1) = 11
max_pie = 36

* solve a formula *
 - h = n // 2 = 5
 - v = n - h  = 5
max_pie = (h + 1) * (v + 1) = 36
```
