import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_moves, run_min_moves
    from solution import Solution

    return Solution, assert_min_moves, run_min_moves


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums, run_min_moves):
    result = run_min_moves(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_min_moves, expected, result):
    assert_min_moves(result, expected)
    return


if __name__ == "__main__":
    app.run()
