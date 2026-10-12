#!/usr/bin/env python3

result = ""
for i in range(97, 123):
    char = chr(i)
    if char != 'e' and char != 'q':
        result += char
print(result)
