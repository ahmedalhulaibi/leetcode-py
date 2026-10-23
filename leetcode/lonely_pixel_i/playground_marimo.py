import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_lonely_pixel, run_find_lonely_pixel
    from solution import Solution

    return Solution, assert_find_lonely_pixel, run_find_lonely_pixel


@app.cell
def _():
    # Example test case
    picture = [["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]
    expected = 3
    return expected, picture


@app.cell
def _(Solution, picture, run_find_lonely_pixel):
    result = run_find_lonely_pixel(Solution, picture)
    result
    return (result,)


@app.cell
def _(assert_find_lonely_pixel, expected, result):
    assert_find_lonely_pixel(result, expected)
    return


if __name__ == "__main__":
    app.run()
