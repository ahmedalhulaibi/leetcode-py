import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_bridge, run_shortest_bridge
    from solution import Solution

    return Solution, assert_shortest_bridge, run_shortest_bridge


@app.cell
def _():
    # Example test case
    grid = [[0, 1], [1, 0]]
    expected = 1
    return expected, grid


@app.cell
def _(Solution, grid, run_shortest_bridge):
    result = run_shortest_bridge(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_shortest_bridge, expected, result):
    assert_shortest_bridge(result, expected)
    return


if __name__ == "__main__":
    app.run()
