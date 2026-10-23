import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sum_of_distances_in_tree, run_sum_of_distances_in_tree
    from solution import Solution

    return (
        Solution,
        assert_sum_of_distances_in_tree,
        run_sum_of_distances_in_tree,
    )


@app.cell
def _():
    # Example test case
    n = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    expected = [8, 12, 6, 10, 10, 10]
    return edges, expected, n


@app.cell
def _(Solution, edges, n, run_sum_of_distances_in_tree):
    result = run_sum_of_distances_in_tree(Solution, n, edges)
    result
    return (result,)


@app.cell
def _(assert_sum_of_distances_in_tree, expected, result):
    assert_sum_of_distances_in_tree(result, expected)
    return


if __name__ == "__main__":
    app.run()
