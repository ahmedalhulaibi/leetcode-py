import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_bipartite, run_is_bipartite
    from solution import Solution

    return Solution, assert_is_bipartite, run_is_bipartite


@app.cell
def _():
    # Example test case
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    expected = True
    return expected, graph


@app.cell
def _(Solution, graph, run_is_bipartite):
    result = run_is_bipartite(Solution, graph)
    result
    return (result,)


@app.cell
def _(assert_is_bipartite, expected, result):
    assert_is_bipartite(result, expected)
    return


if __name__ == "__main__":
    app.run()
