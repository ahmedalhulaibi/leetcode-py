import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_integer_replacement, run_integer_replacement
    from solution import Solution

    return Solution, assert_integer_replacement, run_integer_replacement


@app.cell
def _():
    # Example test case
    n = 8
    expected = 3
    return expected, n


@app.cell
def _(Solution, n, run_integer_replacement):
    result = run_integer_replacement(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_integer_replacement, expected, result):
    assert_integer_replacement(result, expected)
    return


if __name__ == "__main__":
    app.run()
