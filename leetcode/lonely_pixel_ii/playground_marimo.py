import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_black_pixel, run_find_black_pixel
    from solution import Solution

    return Solution, assert_find_black_pixel, run_find_black_pixel


@app.cell
def _():
    # Example test case
    picture = [["W", "B", "W"], ["W", "B", "W"], ["W", "B", "W"]]
    target = 1
    expected = 0
    return expected, picture, target


@app.cell
def _(Solution, picture, run_find_black_pixel, target):
    result = run_find_black_pixel(Solution, picture, target)
    result
    return (result,)


@app.cell
def _(assert_find_black_pixel, expected, result):
    assert_find_black_pixel(result, expected)
    return


if __name__ == "__main__":
    app.run()
