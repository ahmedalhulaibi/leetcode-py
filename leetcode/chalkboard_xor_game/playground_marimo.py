import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_xor_game, run_xor_game
    from solution import Solution

    return Solution, assert_xor_game, run_xor_game


@app.cell
def _():
    # Example test case
    nums = [1, 1, 2]
    expected = False
    return expected, nums


@app.cell
def _(Solution, nums, run_xor_game):
    result = run_xor_game(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_xor_game, expected, result):
    assert_xor_game(result, expected)
    return


if __name__ == "__main__":
    app.run()
