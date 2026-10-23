import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_array_nesting, run_array_nesting
    from solution import Solution

    return Solution, assert_array_nesting, run_array_nesting


@app.cell
def _():
    # Example test case
    nums = [5, 4, 0, 3, 1, 6, 2]
    expected = 4
    return expected, nums


@app.cell
def _(Solution, nums, run_array_nesting):
    result = run_array_nesting(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_array_nesting, expected, result):
    assert_array_nesting(result, expected)
    return


if __name__ == "__main__":
    app.run()
