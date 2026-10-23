import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_rectangle_area, run_rectangle_area
    from solution import Solution

    return Solution, assert_rectangle_area, run_rectangle_area


@app.cell
def _():
    # Example test case
    rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
    expected = 6
    return expected, rectangles


@app.cell
def _(Solution, rectangles, run_rectangle_area):
    result = run_rectangle_area(Solution, rectangles)
    result
    return (result,)


@app.cell
def _(assert_rectangle_area, expected, result):
    assert_rectangle_area(result, expected)
    return


if __name__ == "__main__":
    app.run()
