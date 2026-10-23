import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_triangle_area, run_largest_triangle_area
    from solution import Solution

    return Solution, assert_largest_triangle_area, run_largest_triangle_area


@app.cell
def _():
    # Example test case
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    expected = 2.0
    return expected, points


@app.cell
def _(Solution, points, run_largest_triangle_area):
    result = run_largest_triangle_area(Solution, points)
    result
    return (result,)


@app.cell
def _(assert_largest_triangle_area, expected, result):
    assert_largest_triangle_area(result, expected)
    return


if __name__ == "__main__":
    app.run()
