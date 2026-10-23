import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_width_ramp, run_max_width_ramp
    from solution import Solution

    return Solution, assert_max_width_ramp, run_max_width_ramp


@app.cell
def _():
    # Example test case
    nums = [6, 0, 8, 2, 1, 5]
    expected = 4
    return expected, nums


@app.cell
def _(Solution, nums, run_max_width_ramp):
    result = run_max_width_ramp(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_max_width_ramp, expected, result):
    assert_max_width_ramp(result, expected)
    return


if __name__ == "__main__":
    app.run()
