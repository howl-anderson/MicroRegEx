## 什么是MicroRegEx
MicroRegEx是一个微型的正则表达式引擎.

## 所支持的Operator列表
* `*` - 零次或者更多次重复 
* `+` - 一次或者更多次重复
* `?` - 可选(零次或者一次)
* `a|b` - 匹配a或者b
* `(expr)` - 将`expr`作为原子
* `\` - 转义字符 

## 使用方法 
### 像python内建的regex一样使用
```python
import MicroRegEx

regex = MicroRegEx.compile("(a|b)cd*e?")
result = regex.match("abcde")
print(result)

result = regex.match("acde")
print(result)
```

将会输出:
```text
False
True
```

### 绘制NFA(非确定性有穷状态机)
```python
import MicroRegEx

regex = MicroRegEx.compile("(a|b)c?")
regex.plot()
```

绘制结果如下:
![NFA](img/nfa.png)

### NFA转换成DFA(确定性有穷状态机)
#### NFA to DFA
##### 原始的DFA
```python
import MicroRegEx
from MicroRegEx.Automaton.NFA2DFA import NFA2DFA

nfa = MicroRegEx.compile("(a|b)c?")

dfa = NFA2DFA(nfa).convert()
dfa.plot()
```

绘制结果如下:
![DFA_native](img/dfa_native.png)

##### 简化的DFA
```python
import MicroRegEx
from MicroRegEx.Automaton.NFA2DFA import NFA2DFA

nfa = MicroRegEx.compile("(a|b)c?")

dfa = NFA2DFA(nfa).convert().simplify()
dfa.plot()
```

绘制结果如下:
![DFA_simplified](img/dfa_simplified.png)

#### DFA最小化
##### Brzozowski方法 
```python
import MicroRegEx
from MicroRegEx.Automaton.NFA2DFA import NFA2DFA
from MicroRegEx.Automaton.Minimal.Brzozowski import Brzozowski

nfa = MicroRegEx.compile("(a|b)c?")

dfa = NFA2DFA(nfa).convert().simplify()
mini_dfa = Brzozowski(dfa).construct()
mini_dfa.plot()
```

绘制结果如下:
![DFA_mini](img/dfa_mini.png)

## 致谢与荣誉 
1. 灵感来自[xysun](https://github.com/xysun)的[regex](https://github.com/xysun/regex)项目
2. 少量部分文档来自[lihao98722](https://github.com/lihao98722/)的[regular\_expression\_engine](https://github.com/lihao98722/regular_expression_engine)项目
3. 测试数据来自[Glenn Fowler](http://www.research.att.com/~gsf/testregex/)项目的测试套装.
4. 测试脚本修改自[regex](https://github.com/xysun/regex)项目.
