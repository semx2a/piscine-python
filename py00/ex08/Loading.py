import os
import time


def percentage(part: int, whole: int) -> int:
    Percentage = round(100 * float(part) / float(whole))
    return int(Percentage)


def ft_tqdm(lst: range) -> None:

    totalElems = len(lst)
    size = os.get_terminal_size()
    requiredCharacters = 8 + (len(str(totalElems)) * 2) + 26
    barLength = size.columns - requiredCharacters

    start_time = time.time()

    for currentElem in lst:

        progress = int(round(barLength) * (currentElem + 1) / float(totalElems))

        elapsed_time = time.time() - start_time
        speed = currentElem / elapsed_time if elapsed_time > 0 else 0
        remaining_time = (totalElems - currentElem) / speed if speed > 0 else 0

        elapsed_minutes, elapsed_seconds = divmod(elapsed_time, 60)
        remaining_minutes, remaining_seconds = divmod(remaining_time, 60)

        display = str()
        display += f"{percentage((currentElem + 1), totalElems):3d}"
        display += '%'
        display += '|'
        display += '█' * progress + ' ' * (barLength - progress)
        display += '| '
        display += f'{(currentElem + 1):3d}/{totalElems}'
        display += f' [{elapsed_minutes:02.0f}:{elapsed_seconds:02.0f}<'
        display += f'{remaining_minutes:02.0f}:{remaining_seconds:02.0f}, '
        display += f'{speed:05.02f}it/s]'
        print(display, end='\r')
        yield

    return