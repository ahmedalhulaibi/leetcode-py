import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_smaller, run_count_smaller
    from solution import Solution

    return Solution, assert_count_smaller, run_count_smaller


@app.cell
def _():
    # Example test case
    nums = [5, 2, 6, 1]
    expected = [2, 1, 1, 0]
    return expected, nums


@app.cell
def _(Solution, nums, run_count_smaller):
    result = run_count_smaller(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_count_smaller, expected, result):
    assert_count_smaller(result, expected)
    return


if __name__ == "__main__":
    app.run()
