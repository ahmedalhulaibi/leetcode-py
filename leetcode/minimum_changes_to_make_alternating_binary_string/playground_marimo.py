import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_operations, run_min_operations
    from solution import Solution

    return Solution, assert_min_operations, run_min_operations


@app.cell
def _():
    # Example test case
    s = "0100"
    expected = 1
    return expected, s


@app.cell
def _(Solution, run_min_operations, s):
    result = run_min_operations(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_min_operations, expected, result):
    assert_min_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
