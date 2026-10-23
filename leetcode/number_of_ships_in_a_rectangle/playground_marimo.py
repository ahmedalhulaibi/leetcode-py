import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_ships, run_count_ships
    from solution import Solution

    return Solution, assert_count_ships, run_count_ships


@app.cell
def _():
    # Example test case
    ships = [[1, 1], [2, 2], [3, 3], [5, 5]]
    top_right = [4, 4]
    bottom_left = [0, 0]
    expected = 3
    return bottom_left, expected, ships, top_right


@app.cell
def _(Solution, bottom_left, run_count_ships, ships, top_right):
    result = run_count_ships(Solution, ships, top_right, bottom_left)
    result
    return (result,)


@app.cell
def _(assert_count_ships, expected, result):
    assert_count_ships(result, expected)
    return


if __name__ == "__main__":
    app.run()
