import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_num_edges_to_remove, run_max_num_edges_to_remove
    from solution import Solution

    return (
        Solution,
        assert_max_num_edges_to_remove,
        run_max_num_edges_to_remove,
    )


@app.cell
def _():
    # Example test case
    n = 4
    edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
    expected = 2
    return edges, expected, n


@app.cell
def _(Solution, edges, n, run_max_num_edges_to_remove):
    result = run_max_num_edges_to_remove(Solution, n, edges)
    result
    return (result,)


@app.cell
def _(assert_max_num_edges_to_remove, expected, result):
    assert_max_num_edges_to_remove(result, expected)
    return


if __name__ == "__main__":
    app.run()
