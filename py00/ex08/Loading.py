def percentage(part: int, whole: int):
    Percentage = 100 * float(part) / float(whole)
    yield Percentage


def ft_tqdm(lst: range) -> None:
    n_elem = len(lst)
    for i in lst:
        display = str()
        display += next(percentage(i, n_elem))
        display += '%'
        display += '|'
        display += '='
        display += '|'
        display += f'{i}/{n_elem}'
