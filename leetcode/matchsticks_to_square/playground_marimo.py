import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_makesquare, run_makesquare
    from solution import Solution

    return Solution, assert_makesquare, run_makesquare


@app.cell
def _():
    # Example test case
    matchsticks = [1, 1, 2, 2, 2]
    expected = True
    return expected, matchsticks


@app.cell
def _(Solution, matchsticks, run_makesquare):
    result = run_makesquare(Solution, matchsticks)
    result
    return (result,)


@app.cell
def _(assert_makesquare, expected, result):
    assert_makesquare(result, expected)
    return


if __name__ == "__main__":
    app.run()
