import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_cheapest_jump, run_cheapest_jump
    from solution import Solution

    return Solution, assert_cheapest_jump, run_cheapest_jump


@app.cell
def _():
    # Example test case
    coins = [1, 2, 4, -1, 2]
    max_jump = 2
    expected = [1, 3, 5]
    return coins, expected, max_jump


@app.cell
def _(Solution, coins, max_jump, run_cheapest_jump):
    result = run_cheapest_jump(Solution, coins, max_jump)
    result
    return (result,)


@app.cell
def _(assert_cheapest_jump, expected, result):
    assert_cheapest_jump(result, expected)
    return


if __name__ == "__main__":
    app.run()
