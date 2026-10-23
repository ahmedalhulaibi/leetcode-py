import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reaching_points, run_reaching_points
    from solution import Solution

    return Solution, assert_reaching_points, run_reaching_points


@app.cell
def _():
    # Example test case
    sx = 1
    sy = 1
    tx = 3
    ty = 5
    expected = True
    return expected, sx, sy, tx, ty


@app.cell
def _(Solution, run_reaching_points, sx, sy, tx, ty):
    result = run_reaching_points(Solution, sx, sy, tx, ty)
    result
    return (result,)


@app.cell
def _(assert_reaching_points, expected, result):
    assert_reaching_points(result, expected)
    return


if __name__ == "__main__":
    app.run()
