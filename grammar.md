## The grammar in MicroRegEx
The grammar descriptor will based on yacc-style CFG (Content Free Grammar):

```
expression: pattern;

pattern: subpattern postpattern;

postpattern: none_empty_postpattern | ϵ;
           
none_empty_postpattern: '|' subpattern postpattern;

subpattern: element other;

other: subpattern | ϵ;

element: atom meta_character;

meta_character: '?' | '+' | '*' | ϵ;

atom: atom_pattern | CHARACTER;
    
atom_pattern: '(' pattern ')';
```
