from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

print('\33[1m' + 'Mandatory tests:\n' + '\33[0m')
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))

print('\33[1m' + '\nCustom tests:\n' + '\33[0m')
print(NULL_not_found(0.12))
print(NULL_not_found(1))
print(NULL_not_found(True))
print(NULL_not_found("Test"))
