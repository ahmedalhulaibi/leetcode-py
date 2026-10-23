import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_single_non_duplicate, run_single_non_duplicate
    from solution import Solution

    return Solution, assert_single_non_duplicate, run_single_non_duplicate


@app.cell
def _():
    # Example test case
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums, run_single_non_duplicate):
    result = run_single_non_duplicate(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_single_non_duplicate, expected, result):
    assert_single_non_duplicate(result, expected)
    return


if __name__ == "__main__":
    app.run()
