import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_new21_game, run_new21_game
    from solution import Solution

    return Solution, assert_new21_game, run_new21_game


@app.cell
def _():
    # Example test case
    n = 10
    k = 1
    max_pts = 10
    expected = 1.0
    return expected, k, max_pts, n


@app.cell
def _(Solution, k, max_pts, n, run_new21_game):
    result = run_new21_game(Solution, n, k, max_pts)
    result
    return (result,)


@app.cell
def _(assert_new21_game, expected, result):
    assert_new21_game(result, expected)
    return


if __name__ == "__main__":
    app.run()
