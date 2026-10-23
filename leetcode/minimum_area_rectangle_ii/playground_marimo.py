import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_area_free_rect, run_min_area_free_rect
    from solution import Solution

    return Solution, assert_min_area_free_rect, run_min_area_free_rect


@app.cell
def _():
    # Example test case
    points = [[1, 2], [2, 1], [1, 0], [0, 1]]
    expected = 2.0
    return expected, points


@app.cell
def _(Solution, points, run_min_area_free_rect):
    result = run_min_area_free_rect(Solution, points)
    result
    return (result,)


@app.cell
def _(assert_min_area_free_rect, expected, result):
    assert_min_area_free_rect(result, expected)
    return


if __name__ == "__main__":
    app.run()
