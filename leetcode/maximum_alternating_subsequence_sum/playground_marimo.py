import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_alternating_sum, run_max_alternating_sum
    from solution import Solution

    return Solution, assert_max_alternating_sum, run_max_alternating_sum


@app.cell
def _():
    # Example test case
    nums = [4, 2, 5, 3]
    expected = 7
    return expected, nums


@app.cell
def _(Solution, nums, run_max_alternating_sum):
    result = run_max_alternating_sum(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_max_alternating_sum, expected, result):
    assert_max_alternating_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
