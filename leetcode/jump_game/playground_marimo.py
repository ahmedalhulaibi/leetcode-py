import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_jump, run_can_jump
    from solution import Solution

    return Solution, assert_can_jump, run_can_jump


@app.cell
def _():
    # Example test case
    nums = [2, 3, 1, 1, 4]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_can_jump):
    result = run_can_jump(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_can_jump, expected, result):
    assert_can_jump(result, expected)
    return


if __name__ == "__main__":
    app.run()
