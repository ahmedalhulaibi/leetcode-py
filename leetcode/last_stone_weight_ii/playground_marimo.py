import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_last_stone_weight_ii, run_last_stone_weight_ii
    from solution import Solution

    return Solution, assert_last_stone_weight_ii, run_last_stone_weight_ii


@app.cell
def _():
    # Example test case
    stones = [2, 7, 4, 1, 8, 1]
    expected = 1
    return expected, stones


@app.cell
def _(Solution, run_last_stone_weight_ii, stones):
    result = run_last_stone_weight_ii(Solution, stones)
    result
    return (result,)


@app.cell
def _(assert_last_stone_weight_ii, expected, result):
    assert_last_stone_weight_ii(result, expected)
    return


if __name__ == "__main__":
    app.run()
