import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_cost_tickets, run_min_cost_tickets
    from solution import Solution

    return Solution, assert_min_cost_tickets, run_min_cost_tickets


@app.cell
def _():
    # Example test case
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    expected = 11
    return costs, days, expected


@app.cell
def _(Solution, costs, days, run_min_cost_tickets):
    result = run_min_cost_tickets(Solution, days, costs)
    result
    return (result,)


@app.cell
def _(assert_min_cost_tickets, expected, result):
    assert_min_cost_tickets(result, expected)
    return


if __name__ == "__main__":
    app.run()
