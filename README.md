# python_easy2use
To store and share some handmade functions which make python more easy to use.

## function list
### print\_pointer
Print a list and print the pointer of this list.
It helps when you learning algorithm.
- Arguments
  - `data`, it must be a List
  - `up_pointer_list`, it must be a list of integer, default is `[]`
  - `down_pointer_list`, it must be a list of integer, default is `[]`
  - `up_pointer`, it must be a string, defalut is `^`
  - `down_pointer`, it must be a list of integer, default is 'v'
#### example
```python
from easy2use_func.easy2use_func import print_pointer
from random import randint
a = [randint(1,20) for i in range(20)]
left_pointer = 0
right_pointer = len(a)-1
while left_pointer < 5:
    print_pointer(a,[left_pointer],[right_pointer],'↑','↓')
    left_pointer += 1
    right_pointer -= 2
```
