import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_check, run_check
    from solution import Solution

    return Solution, assert_check, run_check


@app.cell
def _():
    # Example test case
    nums = [3, 4, 5, 1, 2]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_check):
    result = run_check(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_check, expected, result):
    assert_check(result, expected)
    return


if __name__ == "__main__":
    app.run()
