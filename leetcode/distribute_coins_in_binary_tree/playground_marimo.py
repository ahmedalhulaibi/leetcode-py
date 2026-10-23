import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_distribute_coins, run_distribute_coins
    from solution import Solution

    return Solution, assert_distribute_coins, run_distribute_coins


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [3, 0, 0]
    expected = 2
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_distribute_coins):
    result = run_distribute_coins(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_distribute_coins, expected, result):
    assert_distribute_coins(result, expected)
    return


if __name__ == "__main__":
    app.run()
