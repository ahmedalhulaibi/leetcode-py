import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_similar_rgb, run_similar_rgb
    from solution import Solution

    return Solution, assert_similar_rgb, run_similar_rgb


@app.cell
def _():
    # Example test case
    color = "#09f166"
    expected = "#11ee66"
    return color, expected


@app.cell
def _(Solution, color, run_similar_rgb):
    result = run_similar_rgb(Solution, color)
    result
    return (result,)


@app.cell
def _(assert_similar_rgb, expected, result):
    assert_similar_rgb(result, expected)
    return


if __name__ == "__main__":
    app.run()
