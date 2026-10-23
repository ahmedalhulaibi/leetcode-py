import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_duplicates, run_remove_duplicates
    from solution import Solution

    return Solution, assert_remove_duplicates, run_remove_duplicates


@app.cell
def _():
    # Example test case
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected = (5, [0, 1, 2, 3, 4])
    return expected, nums


@app.cell
def _(Solution, nums, run_remove_duplicates):
    result = run_remove_duplicates(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_remove_duplicates, expected, result):
    assert_remove_duplicates(result, expected)
    return


if __name__ == "__main__":
    app.run()
