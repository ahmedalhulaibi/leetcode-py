import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_array_sign, run_array_sign
    from solution import Solution

    return Solution, assert_array_sign, run_array_sign


@app.cell
def _():
    # Example test case
    nums = [-1, -2, -3, -4, 3, 2, 1]
    expected = 1
    return expected, nums


@app.cell
def _(Solution, nums, run_array_sign):
    result = run_array_sign(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_array_sign, expected, result):
    assert_array_sign(result, expected)
    return


if __name__ == "__main__":
    app.run()
