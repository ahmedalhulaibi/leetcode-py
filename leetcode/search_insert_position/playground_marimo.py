import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_search_insert, run_search_insert
    from solution import Solution

    return Solution, assert_search_insert, run_search_insert


@app.cell
def _():
    # Example test case
    nums = [1, 3, 5, 6]
    target = 5
    expected = 2
    return expected, nums, target


@app.cell
def _(Solution, nums, run_search_insert, target):
    result = run_search_insert(Solution, nums, target)
    result
    return (result,)


@app.cell
def _(assert_search_insert, expected, result):
    assert_search_insert(result, expected)
    return


if __name__ == "__main__":
    app.run()
