import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_permute_unique, run_permute_unique
    from solution import Solution

    return Solution, assert_permute_unique, run_permute_unique


@app.cell
def _():
    # Example test case
    nums = [1, 1, 2]
    expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    return expected, nums


@app.cell
def _(Solution, nums, run_permute_unique):
    result = run_permute_unique(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_permute_unique, expected, result):
    assert_permute_unique(result, expected)
    return


if __name__ == "__main__":
    app.run()
