import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_rotate, run_rotate
    from solution import Solution

    return Solution, assert_rotate, run_rotate


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    expected = [5, 6, 7, 1, 2, 3, 4]
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_rotate):
    result = run_rotate(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_rotate, expected, result):
    assert_rotate(result, expected)
    return


if __name__ == "__main__":
    app.run()
