import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_area, run_max_area
    from solution import Solution

    return Solution, assert_max_area, run_max_area


@app.cell
def _():
    # Example test case
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    expected = 49
    return expected, height


@app.cell
def _(Solution, height, run_max_area):
    result = run_max_area(Solution, height)
    result
    return (result,)


@app.cell
def _(assert_max_area, expected, result):
    assert_max_area(result, expected)
    return


if __name__ == "__main__":
    app.run()
