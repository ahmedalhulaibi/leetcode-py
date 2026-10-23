import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sort_colors, run_sort_colors
    from solution import Solution

    return Solution, assert_sort_colors, run_sort_colors


@app.cell
def _():
    # Example test case
    nums = [2, 0, 2, 1, 1, 0]
    expected = [0, 0, 1, 1, 2, 2]
    return expected, nums


@app.cell
def _(Solution, nums, run_sort_colors):
    result = run_sort_colors(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_sort_colors, expected, result):
    assert_sort_colors(result, expected)
    return


if __name__ == "__main__":
    app.run()
