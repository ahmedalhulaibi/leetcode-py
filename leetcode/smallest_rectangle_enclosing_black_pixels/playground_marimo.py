import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_area, run_min_area
    from solution import Solution

    return Solution, assert_min_area, run_min_area


@app.cell
def _():
    # Example test case
    image = [["0", "0", "1", "0"], ["0", "1", "1", "0"], ["0", "1", "0", "0"]]
    x = 0
    y = 2
    expected = 6
    return expected, image, x, y


@app.cell
def _(Solution, image, run_min_area, x, y):
    result = run_min_area(Solution, image, x, y)
    result
    return (result,)


@app.cell
def _(assert_min_area, expected, result):
    assert_min_area(result, expected)
    return


if __name__ == "__main__":
    app.run()
