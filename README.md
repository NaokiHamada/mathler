# mathler
[Mathler](https://mathler.com/)のソルバです．

## Requirements
Python 3.6+

## Usage
式を入力すると答えを見つけてくれます．
```
$ python mathler.py 153*3-47
Find the hidden calculation that equals 412

Trial = 1/6
Guess = 1+23+388
Hint  = !__?_?__

Trial = 2/6
Guess = 133*3+13
Hint  = !_!!!___

Trial = 3/6
Guess = 143*3-17
Hint  = !?!!!!_!

Trial = 4/6
Guess = 153*3-47
Hint  = !!!!!!!!

Solved: 153*3-47
```

## FAQ
- 式とヒントを与えたら次のGuessを出してくれる機能がほしいです．
    - 本家のスポイラーになっちゃうのであえて実装してませんが，このプログラムを少し改造すれば作れます．
