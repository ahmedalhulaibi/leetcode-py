import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_the_city, run_find_the_city
    from solution import Solution

    return Solution, assert_find_the_city, run_find_the_city


@app.cell
def _():
    # Example test case
    n = 4
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    distance_threshold = 4
    expected = 3
    return distance_threshold, edges, expected, n


@app.cell
def _(Solution, distance_threshold, edges, n, run_find_the_city):
    result = run_find_the_city(Solution, n, edges, distance_threshold)
    result
    return (result,)


@app.cell
def _(assert_find_the_city, expected, result):
    assert_find_the_city(result, expected)
    return


if __name__ == "__main__":
    app.run()
