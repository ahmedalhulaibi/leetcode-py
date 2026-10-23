import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_swaps, run_min_swaps
    from solution import Solution

    return Solution, assert_min_swaps, run_min_swaps


@app.cell
def _():
    # Example test case
    nums = [0, 1, 0, 1, 1, 0, 0]
    expected = 1
    return expected, nums


@app.cell
def _(Solution, nums, run_min_swaps):
    result = run_min_swaps(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_min_swaps, expected, result):
    assert_min_swaps(result, expected)
    return


if __name__ == "__main__":
    app.run()
