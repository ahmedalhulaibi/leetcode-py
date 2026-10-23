import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_stars, run_remove_stars
    from solution import Solution

    return Solution, assert_remove_stars, run_remove_stars


@app.cell
def _():
    # Example test case
    s = "leet**cod*e"
    expected = "lecoe"
    return expected, s


@app.cell
def _(Solution, run_remove_stars, s):
    result = run_remove_stars(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_remove_stars, expected, result):
    assert_remove_stars(result, expected)
    return


if __name__ == "__main__":
    app.run()
