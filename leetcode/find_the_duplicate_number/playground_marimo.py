import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_duplicate, run_find_duplicate
    from solution import Solution

    return Solution, assert_find_duplicate, run_find_duplicate


@app.cell
def _():
    # Example test case
    nums: list[int] = [1, 3, 4, 2, 2]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums: list[int], run_find_duplicate):
    result = run_find_duplicate(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_duplicate, expected, result):
    assert_find_duplicate(result, expected)
    return


if __name__ == "__main__":
    app.run()
