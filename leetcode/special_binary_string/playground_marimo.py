import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_make_largest_special, run_make_largest_special
    from solution import Solution

    return Solution, assert_make_largest_special, run_make_largest_special


@app.cell
def _():
    # Example test case
    s = "11011000"
    expected = "11100100"
    return expected, s


@app.cell
def _(Solution, run_make_largest_special, s):
    result = run_make_largest_special(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_make_largest_special, expected, result):
    assert_make_largest_special(result, expected)
    return


if __name__ == "__main__":
    app.run()
