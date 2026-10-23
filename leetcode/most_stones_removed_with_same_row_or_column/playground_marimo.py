import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_stones, run_remove_stones
    from solution import Solution

    return Solution, assert_remove_stones, run_remove_stones


@app.cell
def _():
    # Example test case
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    expected = 5
    return expected, stones


@app.cell
def _(Solution, run_remove_stones, stones):
    result = run_remove_stones(Solution, stones)
    result
    return (result,)


@app.cell
def _(assert_remove_stones, expected, result):
    assert_remove_stones(result, expected)
    return


if __name__ == "__main__":
    app.run()
