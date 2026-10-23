import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_eventual_safe_nodes, run_eventual_safe_nodes
    from solution import Solution

    return Solution, assert_eventual_safe_nodes, run_eventual_safe_nodes


@app.cell
def _():
    # Example test case
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    expected = [2, 4, 5, 6]
    return expected, graph


@app.cell
def _(Solution, graph, run_eventual_safe_nodes):
    result = run_eventual_safe_nodes(Solution, graph)
    result
    return (result,)


@app.cell
def _(assert_eventual_safe_nodes, expected, result):
    assert_eventual_safe_nodes(result, expected)
    return


if __name__ == "__main__":
    app.run()
