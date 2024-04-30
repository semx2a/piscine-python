import NULL_not_found as nnf

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

print('\33[1m' + 'Mandatory tests:\n' + '\33[0m')
nnf.NULL_not_foundNULL_not_found(Nothing)
nnf.NULL_not_foundNULL_not_found(Garlic)
nnf.NULL_not_foundNULL_not_found(Zero)
nnf.NULL_not_foundNULL_not_found(Empty)
nnf.NULL_not_foundNULL_not_found(Fake)
print(nnf.NULL_not_found("Brian"))

print('\33[1m' + '\nCustom tests:\n' + '\33[0m')
print(nnf.NULL_not_found(0.12))
print(nnf.NULL_not_found(1))
print(nnf.NULL_not_found(True))
print(nnf.NULL_not_found("Test"))
