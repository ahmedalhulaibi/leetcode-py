import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_roman_to_int, run_roman_to_int
    from solution import Solution

    return Solution, assert_roman_to_int, run_roman_to_int


@app.cell
def _():
    # Example test case
    s = "MCMXCIV"
    expected = 1994
    return expected, s


@app.cell
def _(Solution, run_roman_to_int, s):
    result = run_roman_to_int(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_roman_to_int, expected, result):
    assert_roman_to_int(result, expected)
    return


if __name__ == "__main__":
    app.run()
