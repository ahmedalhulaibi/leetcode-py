import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_falling_squares, run_falling_squares
    from solution import Solution

    return Solution, assert_falling_squares, run_falling_squares


@app.cell
def _():
    # Example test case
    positions = [[1, 2], [2, 3], [6, 1]]
    expected = [2, 5, 5]
    return expected, positions


@app.cell
def _(Solution, positions, run_falling_squares):
    result = run_falling_squares(Solution, positions)
    result
    return (result,)


@app.cell
def _(assert_falling_squares, expected, result):
    assert_falling_squares(result, expected)
    return


if __name__ == "__main__":
    app.run()
