import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_super_pow, run_super_pow
    from solution import Solution

    return Solution, assert_super_pow, run_super_pow


@app.cell
def _():
    # Example test case
    a = 2
    b = [1, 0]
    expected = 1024
    return a, b, expected


@app.cell
def _(Solution, a, b, run_super_pow):
    result = run_super_pow(Solution, a, b)
    result
    return (result,)


@app.cell
def _(assert_super_pow, expected, result):
    assert_super_pow(result, expected)
    return


if __name__ == "__main__":
    app.run()
