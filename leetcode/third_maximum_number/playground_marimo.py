import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_third_max, run_third_max
    from solution import Solution

    return Solution, assert_third_max, run_third_max


@app.cell
def _():
    # Example test case
    nums = [3, 2, 1]
    expected = 1
    return expected, nums


@app.cell
def _(Solution, nums, run_third_max):
    result = run_third_max(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_third_max, expected, result):
    assert_third_max(result, expected)
    return


if __name__ == "__main__":
    app.run()
