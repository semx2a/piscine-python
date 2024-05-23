def percentage(part: int, whole: int) -> int:
    Percentage = 100 * float(part) / float(whole)
    yield int(Percentage)


def ft_tqdm(lst: range) -> None:
    n_elem = len(lst)
    for i in lst:
        display = str()
        display += f"{next(percentage(i, n_elem))}"
        display += '%'
        display += '|'
        display += ''.join('=' for j in lst if j < i)
        display += '|'
        display += f'{i}/{n_elem}'
        print(display)
    return lst
