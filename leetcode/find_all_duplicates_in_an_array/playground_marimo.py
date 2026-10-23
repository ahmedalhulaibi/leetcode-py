import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_duplicates, run_find_duplicates
    from solution import Solution

    return Solution, assert_find_duplicates, run_find_duplicates


@app.cell
def _():
    # Example test case
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    expected = [2, 3]
    return expected, nums


@app.cell
def _(Solution, nums, run_find_duplicates):
    result = run_find_duplicates(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_duplicates, expected, result):
    assert_find_duplicates(result, expected)
    return


if __name__ == "__main__":
    app.run()
