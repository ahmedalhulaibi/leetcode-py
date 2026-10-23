import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_score, run_min_score
    from solution import Solution

    return Solution, assert_min_score, run_min_score


@app.cell
def _():
    # Example test case
    n = 4
    roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]
    expected = 5
    return expected, n, roads


@app.cell
def _(Solution, n, roads, run_min_score):
    result = run_min_score(Solution, n, roads)
    result
    return (result,)


@app.cell
def _(assert_min_score, expected, result):
    assert_min_score(result, expected)
    return


if __name__ == "__main__":
    app.run()
