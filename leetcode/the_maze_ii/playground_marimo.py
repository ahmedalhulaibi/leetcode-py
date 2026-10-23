import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_distance, run_shortest_distance
    from solution import Solution

    return Solution, assert_shortest_distance, run_shortest_distance


@app.cell
def _():
    # Example test case
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 4]
    destination = [4, 4]
    expected = 12
    return destination, expected, maze, start


@app.cell
def _(Solution, destination, maze, run_shortest_distance, start):
    result = run_shortest_distance(Solution, maze, start, destination)
    result
    return (result,)


@app.cell
def _(assert_shortest_distance, expected, result):
    assert_shortest_distance(result, expected)
    return


if __name__ == "__main__":
    app.run()
