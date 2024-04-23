def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)
    ret = None

    try:
        match object:
            case str():
                ret = f'{object} is in the kitchen : {obj_type}'
            case list():
                ret = f'List: {obj_type}'
            case tuple():
                ret = f'Tuple: {obj_type}'
            case set():
                ret = f'Set: {obj_type}'
            case dict():
                ret = f'Dict: {obj_type}'
            case _:
                ret = "Type not found"

        if ret is not None:
            print(ret)
    except Exception as e:
        print(f"Error: {e}")
    return 42
