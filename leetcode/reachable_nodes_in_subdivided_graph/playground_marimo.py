import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reachable_nodes, run_reachable_nodes
    from solution import Solution

    return Solution, assert_reachable_nodes, run_reachable_nodes


@app.cell
def _():
    # Example test case
    edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2]]
    max_moves = 6
    n = 3
    expected = 13
    return edges, expected, max_moves, n


@app.cell
def _(Solution, edges, max_moves, n, run_reachable_nodes):
    result = run_reachable_nodes(Solution, edges, max_moves, n)
    result
    return (result,)


@app.cell
def _(assert_reachable_nodes, expected, result):
    assert_reachable_nodes(result, expected)
    return


if __name__ == "__main__":
    app.run()
