import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_gain, run_maximum_gain
    from solution import Solution

    return Solution, assert_maximum_gain, run_maximum_gain


@app.cell
def _():
    # Example test case
    s = "cdbcbbaaabab"
    x = 4
    y = 5
    expected = 19
    return expected, s, x, y


@app.cell
def _(Solution, run_maximum_gain, s, x, y):
    result = run_maximum_gain(Solution, s, x, y)
    result
    return (result,)


@app.cell
def _(assert_maximum_gain, expected, result):
    assert_maximum_gain(result, expected)
    return


if __name__ == "__main__":
    app.run()
