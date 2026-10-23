import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_path_length, run_shortest_path_length
    from solution import Solution

    return Solution, assert_shortest_path_length, run_shortest_path_length


@app.cell
def _():
    # Example test case
    graph = [[1, 2, 3], [0], [0], [0]]
    expected = 4
    return expected, graph


@app.cell
def _(Solution, graph, run_shortest_path_length):
    result = run_shortest_path_length(Solution, graph)
    result
    return (result,)


@app.cell
def _(assert_shortest_path_length, expected, result):
    assert_shortest_path_length(result, expected)
    return


if __name__ == "__main__":
    app.run()
