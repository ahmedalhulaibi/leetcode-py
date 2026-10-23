import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_jump, run_jump
    from solution import Solution

    return Solution, assert_jump, run_jump


@app.cell
def _():
    # Example test case
    nums: list[int] = [2, 3, 1, 1, 4]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums: list[int], run_jump):
    result = run_jump(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_jump, expected, result):
    assert_jump(result, expected)
    return


if __name__ == "__main__":
    app.run()
