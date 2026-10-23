import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_pivot_index, run_pivot_index
    from solution import Solution

    return Solution, assert_pivot_index, run_pivot_index


@app.cell
def _():
    # Example test case
    nums = [1, 7, 3, 6, 5, 6]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums, run_pivot_index):
    result = run_pivot_index(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_pivot_index, expected, result):
    assert_pivot_index(result, expected)
    return


if __name__ == "__main__":
    app.run()
