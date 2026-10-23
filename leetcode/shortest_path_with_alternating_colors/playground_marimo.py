import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_alternating_paths, run_shortest_alternating_paths
    from solution import Solution

    return (
        Solution,
        assert_shortest_alternating_paths,
        run_shortest_alternating_paths,
    )


@app.cell
def _():
    # Example test case
    n = 3
    red_edges = [[0, 1], [1, 2]]
    blue_edges = []
    expected = [0, 1, -1]
    return blue_edges, expected, n, red_edges


@app.cell
def _(Solution, blue_edges, n, red_edges, run_shortest_alternating_paths):
    result = run_shortest_alternating_paths(Solution, n, red_edges, blue_edges)
    result
    return (result,)


@app.cell
def _(assert_shortest_alternating_paths, expected, result):
    assert_shortest_alternating_paths(result, expected)
    return


if __name__ == "__main__":
    app.run()
