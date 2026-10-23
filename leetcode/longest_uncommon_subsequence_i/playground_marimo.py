import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_luslength, run_find_luslength
    from solution import Solution

    return Solution, assert_find_luslength, run_find_luslength


@app.cell
def _():
    # Example test case
    a = "aba"
    b = "cdc"
    expected = 3
    return a, b, expected


@app.cell
def _(Solution, a, b, run_find_luslength):
    result = run_find_luslength(Solution, a, b)
    result
    return (result,)


@app.cell
def _(assert_find_luslength, expected, result):
    assert_find_luslength(result, expected)
    return


if __name__ == "__main__":
    app.run()
