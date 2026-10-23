import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_best_rotation, run_best_rotation
    from solution import Solution

    return Solution, assert_best_rotation, run_best_rotation


@app.cell
def _():
    # Example test case
    nums = [2, 3, 1, 4, 0]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums, run_best_rotation):
    result = run_best_rotation(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_best_rotation, expected, result):
    assert_best_rotation(result, expected)
    return


if __name__ == "__main__":
    app.run()
