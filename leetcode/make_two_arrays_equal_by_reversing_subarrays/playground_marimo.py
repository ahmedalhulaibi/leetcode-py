import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_be_equal, run_can_be_equal
    from solution import Solution

    return Solution, assert_can_be_equal, run_can_be_equal


@app.cell
def _():
    # Example test case
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    expected = True
    return arr, expected, target


@app.cell
def _(Solution, arr, run_can_be_equal, target):
    result = run_can_be_equal(Solution, target, arr)
    result
    return (result,)


@app.cell
def _(assert_can_be_equal, expected, result):
    assert_can_be_equal(result, expected)
    return


if __name__ == "__main__":
    app.run()
