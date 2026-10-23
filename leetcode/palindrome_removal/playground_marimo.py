import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_moves, run_minimum_moves
    from solution import Solution

    return Solution, assert_minimum_moves, run_minimum_moves


@app.cell
def _():
    # Example test case
    arr = [1, 3, 4, 1, 5]
    expected = 3
    return arr, expected


@app.cell
def _(Solution, arr, run_minimum_moves):
    result = run_minimum_moves(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_minimum_moves, expected, result):
    assert_minimum_moves(result, expected)
    return


if __name__ == "__main__":
    app.run()
