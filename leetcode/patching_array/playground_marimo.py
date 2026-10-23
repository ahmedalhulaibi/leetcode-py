import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_patches, run_min_patches
    from solution import Solution

    return Solution, assert_min_patches, run_min_patches


@app.cell
def _():
    # Example test case
    nums = [1, 3]
    n = 6
    expected = 1
    return expected, n, nums


@app.cell
def _(Solution, n, nums, run_min_patches):
    result = run_min_patches(Solution, nums, n)
    result
    return (result,)


@app.cell
def _(assert_min_patches, expected, result):
    assert_min_patches(result, expected)
    return


if __name__ == "__main__":
    app.run()
