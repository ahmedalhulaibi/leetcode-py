import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_area_rect, run_min_area_rect
    from solution import Solution

    return Solution, assert_min_area_rect, run_min_area_rect


@app.cell
def _():
    # Example test case
    points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
    expected = 4
    return expected, points


@app.cell
def _(Solution, points, run_min_area_rect):
    result = run_min_area_rect(Solution, points)
    result
    return (result,)


@app.cell
def _(assert_min_area_rect, expected, result):
    assert_min_area_rect(result, expected)
    return


if __name__ == "__main__":
    app.run()
