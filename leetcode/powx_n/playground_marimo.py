import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_my_pow, run_my_pow
    from solution import Solution

    return Solution, assert_my_pow, run_my_pow


@app.cell
def _():
    # Example test case
    x = 2.0
    n = 10
    expected = 1024.0
    return expected, n, x


@app.cell
def _(Solution, n, run_my_pow, x):
    result = run_my_pow(Solution, x, n)
    result
    return (result,)


@app.cell
def _(assert_my_pow, expected, result):
    assert_my_pow(result, expected)
    return


if __name__ == "__main__":
    app.run()
