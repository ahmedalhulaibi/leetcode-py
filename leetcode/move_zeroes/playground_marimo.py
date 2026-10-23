import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_move_zeroes, run_move_zeroes
    from solution import Solution

    return Solution, assert_move_zeroes, run_move_zeroes


@app.cell
def _():
    # Example test case
    nums = [0, 1, 0, 3, 12]
    expected = [1, 3, 12, 0, 0]
    return expected, nums


@app.cell
def _(Solution, nums, run_move_zeroes):
    result = run_move_zeroes(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_move_zeroes, expected, result):
    assert_move_zeroes(result, expected)
    return


if __name__ == "__main__":
    app.run()
