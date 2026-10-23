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
    n = 5
    edges = [[0, 1, 7], [1, 3, 7], [1, 2, 1]]
    query = [[0, 3], [3, 4]]
    expected = [1, -1]
    return edges, expected, n, query


@app.cell
def _(Solution, edges, n, query, run_minimum_cost):
    result = run_minimum_cost(Solution, n, edges, query)
    result
    return (result,)


@app.cell
def _(assert_minimum_cost, expected, result):
    assert_minimum_cost(result, expected)
    return


if __name__ == "__main__":
    app.run()
