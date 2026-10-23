import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_depth, run_max_depth
    from solution import Solution

    return Solution, assert_max_depth, run_max_depth


@app.cell
def _():
    # Example test case
    s = "(1+(2*3)+((8)/4))+1"
    expected = 3
    return expected, s


@app.cell
def _(Solution, run_max_depth, s):
    result = run_max_depth(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_max_depth, expected, result):
    assert_max_depth(result, expected)
    return


if __name__ == "__main__":
    app.run()
