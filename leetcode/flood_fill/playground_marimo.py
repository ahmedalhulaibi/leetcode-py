import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_flood_fill, run_flood_fill
    from solution import Solution

    return Solution, assert_flood_fill, run_flood_fill


@app.cell
def _():
    # Example test case
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    return color, expected, image, sc, sr


@app.cell
def _(Solution, color, image, run_flood_fill, sc, sr):
    result = run_flood_fill(Solution, image, sr, sc, color)
    result
    return (result,)


@app.cell
def _(assert_flood_fill, expected, result):
    assert_flood_fill(result, expected)
    return


if __name__ == "__main__":
    app.run()
