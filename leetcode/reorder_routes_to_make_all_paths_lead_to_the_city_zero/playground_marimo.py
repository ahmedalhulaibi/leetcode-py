import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_reorder, run_min_reorder
    from solution import Solution

    return Solution, assert_min_reorder, run_min_reorder


@app.cell
def _():
    # Example test case
    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    expected = 3
    return connections, expected, n


@app.cell
def _(Solution, connections, n, run_min_reorder):
    result = run_min_reorder(Solution, n, connections)
    result
    return (result,)


@app.cell
def _(assert_min_reorder, expected, result):
    assert_min_reorder(result, expected)
    return


if __name__ == "__main__":
    app.run()
