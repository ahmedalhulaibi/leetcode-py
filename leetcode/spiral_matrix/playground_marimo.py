import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_spiral_order, run_spiral_order
    from solution import Solution

    return Solution, assert_spiral_order, run_spiral_order


@app.cell
def _():
    # Example test case
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    return expected, matrix


@app.cell
def _(Solution, matrix, run_spiral_order):
    result = run_spiral_order(Solution, matrix)
    result
    return (result,)


@app.cell
def _(assert_spiral_order, expected, result):
    assert_spiral_order(result, expected)
    return


if __name__ == "__main__":
    app.run()
