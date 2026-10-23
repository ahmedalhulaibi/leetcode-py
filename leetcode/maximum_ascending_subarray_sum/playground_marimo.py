import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_ascending_sum, run_max_ascending_sum
    from solution import Solution

    return Solution, assert_max_ascending_sum, run_max_ascending_sum


@app.cell
def _():
    # Example test case
    nums = [10, 20, 30, 5, 10, 50]
    expected = 65
    return expected, nums


@app.cell
def _(Solution, nums, run_max_ascending_sum):
    result = run_max_ascending_sum(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_max_ascending_sum, expected, result):
    assert_max_ascending_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
