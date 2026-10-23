import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import (
        assert_find_critical_and_pseudo_critical_edges,
        run_find_critical_and_pseudo_critical_edges,
    )
    from solution import Solution

    return (
        Solution,
        assert_find_critical_and_pseudo_critical_edges,
        run_find_critical_and_pseudo_critical_edges,
    )


@app.cell
def _():
    # Example test case
    n = 5
    edges = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
    expected = [[0, 1], [2, 3, 4, 5]]
    return edges, expected, n


@app.cell
def _(Solution, edges, n, run_find_critical_and_pseudo_critical_edges):
    result = run_find_critical_and_pseudo_critical_edges(Solution, n, edges)
    result
    return (result,)


@app.cell
def _(assert_find_critical_and_pseudo_critical_edges, expected, result):
    assert_find_critical_and_pseudo_critical_edges(result, expected)
    return


if __name__ == "__main__":
    app.run()
