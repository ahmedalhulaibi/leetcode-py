import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_convex, run_is_convex
    from solution import Solution

    return Solution, assert_is_convex, run_is_convex


@app.cell
def _():
    # Example test case
    points = [[0, 0], [0, 5], [5, 5], [5, 0]]
    expected = True
    return expected, points


@app.cell
def _(Solution, points, run_is_convex):
    result = run_is_convex(Solution, points)
    result
    return (result,)


@app.cell
def _(assert_is_convex, expected, result):
    assert_is_convex(result, expected)
    return


if __name__ == "__main__":
    app.run()
