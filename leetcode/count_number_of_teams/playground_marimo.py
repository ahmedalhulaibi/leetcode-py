import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_teams, run_num_teams
    from solution import Solution

    return Solution, assert_num_teams, run_num_teams


@app.cell
def _():
    # Example test case
    rating = [2, 5, 3, 4, 1]
    expected = 3
    return expected, rating


@app.cell
def _(Solution, rating, run_num_teams):
    result = run_num_teams(Solution, rating)
    result
    return (result,)


@app.cell
def _(assert_num_teams, expected, result):
    assert_num_teams(result, expected)
    return


if __name__ == "__main__":
    app.run()
