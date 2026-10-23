import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reverse, run_reverse
    from solution import Solution

    return Solution, assert_reverse, run_reverse


@app.cell
def _():
    # Example test case
    x = 123
    expected = 321
    return expected, x


@app.cell
def _(Solution, run_reverse, x):
    result = run_reverse(Solution, x)
    result
    return (result,)


@app.cell
def _(assert_reverse, expected, result):
    assert_reverse(result, expected)
    return


if __name__ == "__main__":
    app.run()
