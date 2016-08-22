## Description
Lopy is an MIT Scheme interpreter which creation was inspired by SICP book. 
## How to use it?
Currenly, two modes are supported. 
REPL:
```python
python3 lopy/lo.py
```
And source from file mode:
```python
python3 lopy/lo.py -f example.rkt
python3 lopy/lo.py --file example.rkt
```
## TODO
1. Parser should return some kind of special object instead of application if the following cases (marked with []):
    * ```(define [(f a)] (+ 1 2)) ``` 
    * ```(lambda [(a b)] (* a b))```
    * ```(cond [((= 1 1) 1)] [(else 2)])```
2. Addition of new syntactic forms/builtin procedures from arbitrary file (without editing files in lopy/expressions/ dir
