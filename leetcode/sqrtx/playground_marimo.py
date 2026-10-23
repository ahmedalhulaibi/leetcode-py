import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_my_sqrt, run_my_sqrt
    from solution import Solution

    return Solution, assert_my_sqrt, run_my_sqrt


@app.cell
def _():
    # Example test case
    x = 4
    expected = 2
    return expected, x


@app.cell
def _(Solution, run_my_sqrt, x):
    result = run_my_sqrt(Solution, x)
    result
    return (result,)


@app.cell
def _(assert_my_sqrt, expected, result):
    assert_my_sqrt(result, expected)
    return


if __name__ == "__main__":
    app.run()
