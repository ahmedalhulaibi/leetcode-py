import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_best_team_score, run_best_team_score
    from solution import Solution

    return Solution, assert_best_team_score, run_best_team_score


@app.cell
def _():
    # Example test case
    scores = [1, 3, 5, 10, 15]
    ages = [1, 2, 3, 4, 5]
    expected = 34
    return ages, expected, scores


@app.cell
def _(Solution, ages, run_best_team_score, scores):
    result = run_best_team_score(Solution, scores, ages)
    result
    return (result,)


@app.cell
def _(assert_best_team_score, expected, result):
    assert_best_team_score(result, expected)
    return


if __name__ == "__main__":
    app.run()
