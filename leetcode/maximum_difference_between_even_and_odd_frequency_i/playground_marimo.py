import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_difference, run_max_difference
    from solution import Solution

    return Solution, assert_max_difference, run_max_difference


@app.cell
def _():
    # Example test case
    s = "aaaaabbc"
    expected = 3
    return expected, s


@app.cell
def _(Solution, run_max_difference, s):
    result = run_max_difference(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_max_difference, expected, result):
    assert_max_difference(result, expected)
    return


if __name__ == "__main__":
    app.run()
