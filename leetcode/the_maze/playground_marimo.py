import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_has_path, run_has_path
    from solution import Solution

    return Solution, assert_has_path, run_has_path


@app.cell
def _():
    # Example test case
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 4]
    destination = [4, 4]
    expected = True
    return destination, expected, maze, start


@app.cell
def _(Solution, destination, maze, run_has_path, start):
    result = run_has_path(Solution, maze, start, destination)
    result
    return (result,)


@app.cell
def _(assert_has_path, expected, result):
    assert_has_path(result, expected)
    return


if __name__ == "__main__":
    app.run()
