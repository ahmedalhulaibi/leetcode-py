import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_shortest_way, run_find_shortest_way
    from solution import Solution

    return Solution, assert_find_shortest_way, run_find_shortest_way


@app.cell
def _():
    # Example test case
    maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
    ball = [4, 3]
    hole = [0, 1]
    expected = "lul"
    return ball, expected, hole, maze


@app.cell
def _(Solution, ball, hole, maze, run_find_shortest_way):
    result = run_find_shortest_way(Solution, maze, ball, hole)
    result
    return (result,)


@app.cell
def _(assert_find_shortest_way, expected, result):
    assert_find_shortest_way(result, expected)
    return


if __name__ == "__main__":
    app.run()
