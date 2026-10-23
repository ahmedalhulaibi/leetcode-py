import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_cost, run_minimum_cost
    from solution import Solution

    return Solution, assert_minimum_cost, run_minimum_cost


@app.cell
def _():
    # Example test case
    n = 3
    connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
    expected = 6
    return connections, expected, n


@app.cell
def _(Solution, connections, n, run_minimum_cost):
    result = run_minimum_cost(Solution, n, connections)
    result
    return (result,)


@app.cell
def _(assert_minimum_cost, expected, result):
    assert_minimum_cost(result, expected)
    return


if __name__ == "__main__":
    app.run()
