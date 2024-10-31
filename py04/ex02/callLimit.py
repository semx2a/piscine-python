def callLimit(limit: int):
    """
    A decorator to limit the number of times a function can be called.

    Parameters:
    limit (int): The maximum number of times the decorated function can be
    called.

    Returns:
    function: A decorator that limits the number of calls to the decorated
    function.
    """
    count = 0

    def callLimiter(function):
        """
        Inner decorator function that wraps the target function.

        Parameters:
        function (function): The function to be decorated.

        Returns:
        function: The wrapped function with call limiting applied.
        """
        def limit_function(*args: any, **kwds: any):
            """
            Wrapper function that enforces the call limit.

            Parameters:
            *args (any): Positional arguments to pass to the target function.
            **kwds (any): Keyword arguments to pass to the target function.

            Returns:
            function: The target function if the call limit has not been
            exceeded.
            Prints an error message if the call limit is exceeded.
            """
            nonlocal count
            if count < limit:
                count += 1
                function(*args, **kwds)
            else:
                print(f"Error {function} called too many times")
            return function

        return limit_function

    return callLimiter
