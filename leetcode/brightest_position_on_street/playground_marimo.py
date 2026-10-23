import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_brightest_position, run_brightest_position
    from solution import Solution

    return Solution, assert_brightest_position, run_brightest_position


@app.cell
def _():
    # Example test case
    lights: list[list[int]] = [[-3, 2], [1, 2], [3, 3]]
    expected: int = -1
    return expected, lights


@app.cell
def _(Solution, lights: list[list[int]], run_brightest_position):
    result = run_brightest_position(Solution, lights)
    result
    return (result,)


@app.cell
def _(assert_brightest_position, expected: int, result):
    assert_brightest_position(result, expected)
    return


if __name__ == "__main__":
    app.run()
