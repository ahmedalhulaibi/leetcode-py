import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_score, run_max_score
    from solution import Solution

    return Solution, assert_max_score, run_max_score


@app.cell
def _():
    # Example test case
    card_points = [1, 2, 3, 4, 5, 6, 1]
    k = 3
    expected = 12
    return card_points, expected, k


@app.cell
def _(Solution, card_points, k, run_max_score):
    result = run_max_score(Solution, card_points, k)
    result
    return (result,)


@app.cell
def _(assert_max_score, expected, result):
    assert_max_score(result, expected)
    return


if __name__ == "__main__":
    app.run()
