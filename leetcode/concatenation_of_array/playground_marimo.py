import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_concatenation, run_get_concatenation
    from solution import Solution

    return Solution, assert_get_concatenation, run_get_concatenation


@app.cell
def _():
    # Example test case
    nums = [1, 2, 1]
    expected = [1, 2, 1, 1, 2, 1]
    return expected, nums


@app.cell
def _(Solution, nums, run_get_concatenation):
    result = run_get_concatenation(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_get_concatenation, expected, result):
    assert_get_concatenation(result, expected)
    return


if __name__ == "__main__":
    app.run()
