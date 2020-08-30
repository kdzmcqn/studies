```mermaid
graph BT
1[BaseException]
2[Exception]
3[StandardError]
4[Warning]
31[EOFError]
32[ZeroDivsionError]
33[IndentationError]
41[DeprecatedWarning]
42[ImportWarning]
41 & 42-->4
31 & 32 & 33-->3
3 & 4-->2
2-->1
```