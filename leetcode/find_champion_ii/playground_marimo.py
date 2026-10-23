import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_champion, run_find_champion
    from solution import Solution

    return Solution, assert_find_champion, run_find_champion


@app.cell
def _():
    # Example test case
    n = 3
    edges = [[0, 1], [1, 2]]
    expected = 0
    return edges, expected, n


@app.cell
def _(Solution, edges, n, run_find_champion):
    result = run_find_champion(Solution, n, edges)
    result
    return (result,)


@app.cell
def _(assert_find_champion, expected, result):
    assert_find_champion(result, expected)
    return


if __name__ == "__main__":
    app.run()
