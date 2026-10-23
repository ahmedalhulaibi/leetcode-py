import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_possible, run_is_possible
    from solution import Solution

    return Solution, assert_is_possible, run_is_possible


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 3, 4, 5]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_is_possible):
    result = run_is_possible(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_is_possible, expected, result):
    assert_is_possible(result, expected)
    return


if __name__ == "__main__":
    app.run()
