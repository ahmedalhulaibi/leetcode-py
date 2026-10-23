import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_array_special, run_is_array_special
    from solution import Solution

    return Solution, assert_is_array_special, run_is_array_special


@app.cell
def _():
    # Example test case
    nums = [2, 1, 4]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_is_array_special):
    result = run_is_array_special(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_is_array_special, expected, result):
    assert_is_array_special(result, expected)
    return


if __name__ == "__main__":
    app.run()
