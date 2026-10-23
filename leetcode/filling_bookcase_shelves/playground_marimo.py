import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_height_shelves, run_min_height_shelves
    from solution import Solution

    return Solution, assert_min_height_shelves, run_min_height_shelves


@app.cell
def _():
    # Example test case
    books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
    shelf_width = 4
    expected = 6
    return books, expected, shelf_width


@app.cell
def _(Solution, books, run_min_height_shelves, shelf_width):
    result = run_min_height_shelves(Solution, books, shelf_width)
    result
    return (result,)


@app.cell
def _(assert_min_height_shelves, expected, result):
    assert_min_height_shelves(result, expected)
    return


if __name__ == "__main__":
    app.run()
