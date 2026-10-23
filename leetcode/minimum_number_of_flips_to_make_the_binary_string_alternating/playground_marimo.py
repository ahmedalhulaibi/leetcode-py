import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_flips, run_min_flips
    from solution import Solution

    return Solution, assert_min_flips, run_min_flips


@app.cell
def _():
    # Example test case
    s = "111000"
    expected = 2
    return expected, s


@app.cell
def _(Solution, run_min_flips, s):
    result = run_min_flips(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_min_flips, expected, result):
    assert_min_flips(result, expected)
    return


if __name__ == "__main__":
    app.run()
