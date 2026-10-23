import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_path_binary_matrix, run_shortest_path_binary_matrix
    from solution import Solution

    return (
        Solution,
        assert_shortest_path_binary_matrix,
        run_shortest_path_binary_matrix,
    )


@app.cell
def _():
    # Example test case
    grid = [[0, 1], [1, 0]]
    expected = 2
    return expected, grid


@app.cell
def _(Solution, grid, run_shortest_path_binary_matrix):
    result = run_shortest_path_binary_matrix(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_shortest_path_binary_matrix, expected, result):
    assert_shortest_path_binary_matrix(result, expected)
    return


if __name__ == "__main__":
    app.run()
