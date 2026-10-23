import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_two_city_sched_cost, run_two_city_sched_cost
    from solution import Solution

    return Solution, assert_two_city_sched_cost, run_two_city_sched_cost


@app.cell
def _():
    # Example test case
    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    expected = 110
    return costs, expected


@app.cell
def _(Solution, costs, run_two_city_sched_cost):
    result = run_two_city_sched_cost(Solution, costs)
    result
    return (result,)


@app.cell
def _(assert_two_city_sched_cost, expected, result):
    assert_two_city_sched_cost(result, expected)
    return


if __name__ == "__main__":
    app.run()
