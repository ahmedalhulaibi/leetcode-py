import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_walls_and_gates, run_walls_and_gates
    from solution import Solution

    return Solution, assert_walls_and_gates, run_walls_and_gates


@app.cell
def _():
    # Example test case
    rooms = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    expected = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
    return expected, rooms


@app.cell
def _(Solution, rooms, run_walls_and_gates):
    result = run_walls_and_gates(Solution, rooms)
    result
    return (result,)


@app.cell
def _(assert_walls_and_gates, expected, result):
    assert_walls_and_gates(result, expected)
    return


if __name__ == "__main__":
    app.run()
