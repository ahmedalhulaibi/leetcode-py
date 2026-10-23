import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_distribute_candies, run_distribute_candies
    from solution import Solution

    return Solution, assert_distribute_candies, run_distribute_candies


@app.cell
def _():
    # Example test case
    candy_type = [1, 1, 2, 2, 3, 3]
    expected = 3
    return candy_type, expected


@app.cell
def _(Solution, candy_type, run_distribute_candies):
    result = run_distribute_candies(Solution, candy_type)
    result
    return (result,)


@app.cell
def _(assert_distribute_candies, expected, result):
    assert_distribute_candies(result, expected)
    return


if __name__ == "__main__":
    app.run()
