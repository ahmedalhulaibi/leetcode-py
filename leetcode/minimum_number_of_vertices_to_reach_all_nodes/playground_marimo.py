import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_smallest_set_of_vertices, run_find_smallest_set_of_vertices
    from solution import Solution

    return (
        Solution,
        assert_find_smallest_set_of_vertices,
        run_find_smallest_set_of_vertices,
    )


@app.cell
def _():
    # Example test case
    n = 6
    edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
    expected = [0, 3]
    return edges, expected, n


@app.cell
def _(Solution, edges, n, run_find_smallest_set_of_vertices):
    result = run_find_smallest_set_of_vertices(Solution, n, edges)
    result
    return (result,)


@app.cell
def _(assert_find_smallest_set_of_vertices, expected, result):
    assert_find_smallest_set_of_vertices(result, expected)
    return


if __name__ == "__main__":
    app.run()
