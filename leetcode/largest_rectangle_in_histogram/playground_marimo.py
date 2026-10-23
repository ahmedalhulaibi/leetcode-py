import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_rectangle_area, run_largest_rectangle_area
    from solution import Solution

    return Solution, assert_largest_rectangle_area, run_largest_rectangle_area


@app.cell
def _():
    # Example test case
    heights = [2, 1, 5, 6, 2, 3]
    expected = 10
    return expected, heights


@app.cell
def _(Solution, heights, run_largest_rectangle_area):
    result = run_largest_rectangle_area(Solution, heights)
    result
    return (result,)


@app.cell
def _(assert_largest_rectangle_area, expected, result):
    assert_largest_rectangle_area(result, expected)
    return


if __name__ == "__main__":
    app.run()
