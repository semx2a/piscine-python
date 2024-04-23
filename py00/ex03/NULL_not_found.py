import math


def NULL_not_found(object: any) -> int:

    obj_type = type(object)
    output = None
    ret = 1

    try:
        if not object or (obj_type == float and math.isnan(object)):
            match object:
                case str():
                    output = 'Empty: '
                case float():
                    output = 'Cheese: '
                case bool():
                    output = 'Fake: '
                case int():
                    output = 'Zero: '
                case None:
                    output = 'Nothing: '
                case _:
                    pass
            output += f'{object} {obj_type}'
            ret = 0
        else:
            output = "Type not found"

        if output is not None:
            print(output)
    except Exception as e:
        print(f"Error: {e}")
    return ret
