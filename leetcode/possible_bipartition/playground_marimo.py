import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_possible_bipartition, run_possible_bipartition
    from solution import Solution

    return Solution, assert_possible_bipartition, run_possible_bipartition


@app.cell
def _():
    # Example test case
    n = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]
    expected = True
    return dislikes, expected, n


@app.cell
def _(Solution, dislikes, n, run_possible_bipartition):
    result = run_possible_bipartition(Solution, n, dislikes)
    result
    return (result,)


@app.cell
def _(assert_possible_bipartition, expected, result):
    assert_possible_bipartition(result, expected)
    return


if __name__ == "__main__":
    app.run()
