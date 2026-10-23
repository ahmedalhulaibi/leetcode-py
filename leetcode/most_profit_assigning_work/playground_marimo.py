import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_profit_assignment, run_max_profit_assignment
    from solution import Solution

    return Solution, assert_max_profit_assignment, run_max_profit_assignment


@app.cell
def _():
    # Example test case
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    expected = 100
    return difficulty, expected, profit, worker


@app.cell
def _(Solution, difficulty, profit, run_max_profit_assignment, worker):
    result = run_max_profit_assignment(Solution, difficulty, profit, worker)
    result
    return (result,)


@app.cell
def _(assert_max_profit_assignment, expected, result):
    assert_max_profit_assignment(result, expected)
    return


if __name__ == "__main__":
    app.run()
