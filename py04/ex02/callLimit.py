def callLimit(limit: int):
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count < limit:
                count += 1
                function(*args, **kwds)
            else:
                print(f"Error {function} called too many times")
            return function

        return limit_function

    return callLimiter
