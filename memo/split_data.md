# 分割のルールを見つけるためのデータまとめ

## 定義
![type_of_odd](../docs/images/type-of-odd.png)
![type_of_even](../docs/images/type-of-even.png)

### AとBの数の表

|名前|Odd_A|Odd_B|Even_A|Even_B|
|:-:|:-:|:-:|:-:|:-:|
|step0|0|0|0|0|
|step1|1|0|0|0|
|step2-1|2|0|0|0|
|step2-2|0|1|1|0|
|step2-3|2|0|0|1|
|P1-1ab|1|0|1|1|
|P1-1ac|1|0|1|2|
|P1-2ab|1|1|0|1|
|P1-2ac|1|1|1|1|
|P2-1ab|1|2|0|1|
|P2-2ab|3|0|0|3|
|P2-2cd|3|0|1|0|
|P2-3ab|1|3|1|0|
|P2-3bd|3|0|1|2|
|P3ab|3|0|0|2|
|P3cd|1|2|0|0|
|P5ab(cd)|1|1|1|1|

#### s2-2 to P1-?
|名前|Odd_A|Odd_B|Even_A|Even_B|memo|
|:-:|:-:|:-:|:-:|:-:|:-:|
|step2-2|0|1|1|0||
|P1-1ab|1|0|1|1|OB=OA+EB|
|P1-1ac|1|0|1|2|OB=OA+EB*2|
|P1-2ab|1|1|0|1|EA=OA+EB|
|P1-2ac|1|1|1|1|EA=OA+EB+EA|

#### s2-3 to P2-?
|名前|Odd_A|Odd_B|Even_A|Even_B|memo|
|:-:|:-:|:-:|:-:|:-:|:-:|
|step2-3|2|0|0|1||
|P1-1ab|1|0|1|1|OA=EA|
|P1-1ac|1|0|1|2|OA=EA+EB|
|P1-2ab|1|1|0|1|OA=OB|
|P1-2ac|1|1|1|1|OA=OB+EA|
|P2-1ab|1|2|0|1|OA=OB*2|
|P2-2ab|3|0|0|3|OA+EB*2|
|P2-2cd|3|0|1|0|EB=OA+EA|
|P2-3ab|1|3|1|0|OA+EB=OB*3+EA|
|P2-3bd|3|0|1|2|OA+EA+EB|

#### s2-1 to P3/P5
|名前|Odd_A|Odd_B|Even_A|Even_B|memo|
|:-:|:-:|:-:|:-:|:-:|:-:|
|step2-1|2|0|0|0||
|P3ab|3|0|0|2|OA+EB*2|
|P3cd|1|2|0|0|OA=OB*2|
|P5ab(cd)|1|1|1|1|OA=OB+EA+EB|

### 気づいた点(雑記)
+ 一回のS+で増える頂点は最大3
+ 頂点nのグラフにS+をして生成できるグラフはn^2個
+ stepn -> stepn+1では、3^nこ増える？