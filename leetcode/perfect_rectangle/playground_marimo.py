import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_rectangle_cover, run_is_rectangle_cover
    from solution import Solution

    return Solution, assert_is_rectangle_cover, run_is_rectangle_cover


@app.cell
def _():
    # Example test case
    rectangles: list[list[int]] = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
    expected = True
    return expected, rectangles


@app.cell
def _(Solution, rectangles: list[list[int]], run_is_rectangle_cover):
    result = run_is_rectangle_cover(Solution, rectangles)
    result
    return (result,)


@app.cell
def _(assert_is_rectangle_cover, expected, result):
    assert_is_rectangle_cover(result, expected)
    return


if __name__ == "__main__":
    app.run()
