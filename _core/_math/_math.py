
"""
    core/_math/_math.py

    module designed especially for numbers
    but its not like numpy, numpy is god compared to this

    author: @alexzander
"""

from rich.console import Console
_con = Console()

def fixed_set_precision_str(
    real_number: float | int | str, precision: int):
    """ takes a @real_number and returns it with specified @precision

        return: str version of the number
    """

    # validation
    if not isinstance(real_number, (float, int, str)):
        __message = \
            f"@[yellow]real_number[/]: '[red]{real_number}[/]'" \
            " must be [green]integer[/], [green]float[/], or [green]string[/]"
        _con.print(__message)
        raise TypeError(__message)

    if isinstance(real_number, str):
        try:
            real_number = float(real_number)
        except ValueError as error:
            _con.print(error)
            _con.print(
                f"cannot convert @[yellow]real_number[/]: '[red]{real_number}[/]'"
                " to float")
            raise ValueError(
                f"cannot convert @real_number: '{real_number}'"
                " to float")


    return "{:.{decimals}f}".format(
        real_number,
        decimals=precision
    )


def fixed_set_precision_float(
    real_number: float | str,
    precision: int
):
    """
        takes a @real_number which can be float or string (valid string of a float)

        return: the float with specified @precision as number of decimals
    """
    if isinstance(real_number, str):
        try:
            real_number = float(real_number)
        except ValueError as error:
            _con.print(error)
            _con.print(
                f"cannot convert @[yellow]real_number[/]: '[red]{real_number}[/]'"
                " to float")
            raise ValueError(
                f"cannot convert @real_number: '{real_number}'"
                " to float")

    return float(fixed_set_precision_str(real_number, precision))


def hex_to_int(hex_string: str | int):
    if isinstance(hex_string, int):
        return int(str(hex_string), 16)

    elif isinstance(hex_string, str):
        return int(hex_string, 16)

    else:
        __message = f"@hex_string: '{hex_string}' should be type string or integer"
        _con.print(__message)
        raise TypeError(__message)



