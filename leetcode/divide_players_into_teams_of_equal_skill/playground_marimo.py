import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_divide_players, run_divide_players
    from solution import Solution

    return Solution, assert_divide_players, run_divide_players


@app.cell
def _():
    # Example test case
    skill = [3, 2, 5, 1, 3, 4]
    expected = 22
    return expected, skill


@app.cell
def _(Solution, run_divide_players, skill):
    result = run_divide_players(Solution, skill)
    result
    return (result,)


@app.cell
def _(assert_divide_players, expected, result):
    assert_divide_players(result, expected)
    return


if __name__ == "__main__":
    app.run()
