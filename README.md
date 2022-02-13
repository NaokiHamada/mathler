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
- Q. 解ける問題の規模は？
    - A. 目安としては，文字数が10以下かつ計算結果の絶対値が1000以下ならだいたい6試行以内に解けると思います．本家では符号`+` `-`，冪乗`**`，コメント`//` `/**/`を含む式も回答として受理されますが，今のところ出題された式には含まれていないため，ソルバの生成する式からは除外していますん．
- Q. GuessとHintを与えたら次のGuessを出してくれる機能がほしい．
    - A. 本家のスポイラーになっちゃうのであえて実装してませんが，このプログラムを少し改造すれば作れます．
