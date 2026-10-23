import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_subsets, run_subsets
    from solution import Solution

    return Solution, assert_subsets, run_subsets


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3]
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    return expected, nums


@app.cell
def _(Solution, nums, run_subsets):
    result = run_subsets(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_subsets, expected, result):
    assert_subsets(result, expected)
    return


if __name__ == "__main__":
    app.run()
