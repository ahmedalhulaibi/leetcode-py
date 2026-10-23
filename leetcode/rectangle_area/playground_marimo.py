import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_compute_area, run_compute_area
    from solution import Solution

    return Solution, assert_compute_area, run_compute_area


@app.cell
def _():
    # Example test case
    ax1 = -3
    ay1 = 0
    ax2 = 3
    ay2 = 4
    bx1 = 0
    by1 = -1
    bx2 = 9
    by2 = 2
    expected = 45
    return ax1, ax2, ay1, ay2, bx1, bx2, by1, by2, expected


@app.cell
def _(Solution, ax1, ax2, ay1, ay2, bx1, bx2, by1, by2, run_compute_area):
    result = run_compute_area(Solution, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    result
    return (result,)


@app.cell
def _(assert_compute_area, expected, result):
    assert_compute_area(result, expected)
    return


if __name__ == "__main__":
    app.run()
