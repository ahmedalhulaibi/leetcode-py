import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_clone_graph, run_clone_graph
    from solution import Solution

    return Solution, assert_clone_graph, run_clone_graph


@app.cell
def _():
    # Example test case
    adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
    return (adj_list,)


@app.cell
def _(Solution, adj_list, run_clone_graph):
    result = run_clone_graph(Solution, adj_list)
    result
    return (result,)


@app.cell
def _(adj_list, assert_clone_graph, result):
    assert_clone_graph(result, adj_list)
    return


if __name__ == "__main__":
    app.run()
