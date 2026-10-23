import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_three_equal_parts, run_three_equal_parts
    from solution import Solution

    return Solution, assert_three_equal_parts, run_three_equal_parts


@app.cell
def _():
    # Example test case
    arr = [1, 0, 1, 0, 1]
    expected = [0, 3]
    return arr, expected


@app.cell
def _(Solution, arr, run_three_equal_parts):
    result = run_three_equal_parts(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_three_equal_parts, expected, result):
    assert_three_equal_parts(result, expected)
    return


if __name__ == "__main__":
    app.run()
