import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_contains_duplicate, run_contains_duplicate
    from solution import Solution

    return Solution, assert_contains_duplicate, run_contains_duplicate


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 1]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_contains_duplicate):
    result = run_contains_duplicate(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_contains_duplicate, expected, result):
    assert_contains_duplicate(result, expected)
    return


if __name__ == "__main__":
    app.run()
