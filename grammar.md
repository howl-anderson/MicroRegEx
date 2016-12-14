## The grammar in MicroRegEx
The grammar descriptor will based on yacc-style CFG (Content free Grammar):

```text
expression: pattern;
          
pattern: subpattern postpattern;

postpattern: '|' subpattern postpattern
           | ϵ
           ;

subpattern: element other;

other: subpattern
     | ϵ
     ;

element: atom postfix;

postfix: '?'
       | '+'
       | '*'
       | ϵ
       ;

atom: '(' pattern ')'
    | character
    ;
```
