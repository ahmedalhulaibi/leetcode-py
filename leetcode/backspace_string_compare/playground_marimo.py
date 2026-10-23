import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_backspace_compare, run_backspace_compare
    from solution import Solution

    return Solution, assert_backspace_compare, run_backspace_compare


@app.cell
def _():
    # Example test case
    s = "ab#c"
    t = "ad#c"
    expected = True
    return expected, s, t


@app.cell
def _(Solution, run_backspace_compare, s, t):
    result = run_backspace_compare(Solution, s, t)
    result
    return (result,)


@app.cell
def _(assert_backspace_compare, expected, result):
    assert_backspace_compare(result, expected)
    return


if __name__ == "__main__":
    app.run()
