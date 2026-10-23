import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_matrix, run_find_matrix
    from solution import Solution

    return Solution, assert_find_matrix, run_find_matrix


@app.cell
def _():
    # Example test case
    nums = [1, 3, 4, 1, 2, 3, 1]
    expected = sorted(nums)
    return expected, nums


@app.cell
def _(Solution, nums, run_find_matrix):
    result = run_find_matrix(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_matrix, expected, result):
    assert_find_matrix(result, expected)
    return


if __name__ == "__main__":
    app.run()
