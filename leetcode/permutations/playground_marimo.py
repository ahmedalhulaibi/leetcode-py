import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_permute, run_permute
    from solution import Solution

    return Solution, assert_permute, run_permute


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3]
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    return expected, nums


@app.cell
def _(Solution, nums, run_permute):
    result = run_permute(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_permute, expected, result):
    assert_permute(result, expected)
    return


if __name__ == "__main__":
    app.run()
