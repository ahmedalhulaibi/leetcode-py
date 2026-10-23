import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sort_jumbled, run_sort_jumbled
    from solution import Solution

    return Solution, assert_sort_jumbled, run_sort_jumbled


@app.cell
def _():
    # Example test case
    mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
    nums = [991, 338, 38]
    expected = [338, 38, 991]
    return expected, mapping, nums


@app.cell
def _(Solution, mapping, nums, run_sort_jumbled):
    result = run_sort_jumbled(Solution, mapping, nums)
    result
    return (result,)


@app.cell
def _(assert_sort_jumbled, expected, result):
    assert_sort_jumbled(result, expected)
    return


if __name__ == "__main__":
    app.run()
