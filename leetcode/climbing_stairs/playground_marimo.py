import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_climb_stairs, run_climb_stairs
    from solution import Solution

    return Solution, assert_climb_stairs, run_climb_stairs


@app.cell
def _():
    # Example test case
    n = 3
    expected = 3
    return expected, n


@app.cell
def _(Solution, n, run_climb_stairs):
    result = run_climb_stairs(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_climb_stairs, expected, result):
    assert_climb_stairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
