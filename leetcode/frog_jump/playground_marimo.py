import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_cross, run_can_cross
    from solution import Solution

    return Solution, assert_can_cross, run_can_cross


@app.cell
def _():
    # Example test case
    stones = [0, 1, 3, 5, 6, 8, 12, 17]
    expected = True
    return expected, stones


@app.cell
def _(Solution, run_can_cross, stones):
    result = run_can_cross(Solution, stones)
    result
    return (result,)


@app.cell
def _(assert_can_cross, expected, result):
    assert_can_cross(result, expected)
    return


if __name__ == "__main__":
    app.run()
