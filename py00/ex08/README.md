# Exercise 8: Loading

## Instrcutions

| Files to turn in | Loading.py |
|-------------------|------------|
| Allowed libraries | None |

Make a function called ft_tqdm.
The function must copy the function tqdm with the yield operator.

Here's how it should be prototyped:

```python
def ft_tqdm(lst: range) -> None:`
 pass
```

Your tester.py: (you compare your version with the original)

```python
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
 sleep(0.005)
print()
for elem in tqdm(range(333)):
 sleep(0.005)
print()
```

Expected output:

```sh
$> python tester.py
100%|[===============================================]| 333/333
100%|[                                               ]| 333/333 [00:01<00:00, 191.6it/s]
```

## References

- [Python range() function](https://www.programiz.com/python-programming/methods/built-in/range)
- [Python os.get_terminal_size()](https://www.w3schools.com/python/ref_os_get_terminal_size.asp#:~:text=Python%20os.,-get_terminal_size()%20Method&text=get_terminal_size()%20return%20the%20size,the%20terminal%20window%20in%20characters.)
- [Progress Bar in Python](https://www.geeksforgeeks.org/progress-bars-in-python/)
- [Display numbers with leading zeros](https://stackoverflow.com/questions/134934/display-number-with-leading-zeros)
- [Padding a string in Python](https://www.geeksforgeeks.org/add-padding-to-a-string-in-python/)
