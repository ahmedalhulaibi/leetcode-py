import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_expand, run_expand
    from solution import Solution

    return Solution, assert_expand, run_expand


@app.cell
def _():
    # Example test case
    s = "{a,b}c{d,e}f"
    expected = ["acdf", "acef", "bcdf", "bcef"]
    return expected, s


@app.cell
def _(Solution, run_expand, s):
    result = run_expand(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_expand, expected, result):
    assert_expand(result, expected)
    return


if __name__ == "__main__":
    app.run()
