import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_search_range, run_search_range
    from solution import Solution

    return Solution, assert_search_range, run_search_range


@app.cell
def _():
    # Example test case
    nums: list[int] = [5, 7, 7, 8, 8, 10]
    target = 8
    expected = [3, 4]
    return expected, nums, target


@app.cell
def _(Solution, nums: list[int], run_search_range, target):
    result = run_search_range(Solution, nums, target)
    result
    return (result,)


@app.cell
def _(assert_search_range, expected, result):
    assert_search_range(result, expected)
    return


if __name__ == "__main__":
    app.run()
