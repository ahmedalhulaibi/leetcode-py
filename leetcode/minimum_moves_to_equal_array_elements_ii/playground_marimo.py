import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_moves2, run_min_moves2
    from solution import Solution

    return Solution, assert_min_moves2, run_min_moves2


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums, run_min_moves2):
    result = run_min_moves2(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_min_moves2, expected, result):
    assert_min_moves2(result, expected)
    return


if __name__ == "__main__":
    app.run()
