import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_grid_illumination, run_grid_illumination
    from solution import Solution

    return Solution, assert_grid_illumination, run_grid_illumination


@app.cell
def _():
    # Example test case
    n = 5
    lamps = [[0, 0], [4, 4]]
    queries = [[1, 1], [1, 0]]
    expected = [1, 0]
    return expected, lamps, n, queries


@app.cell
def _(Solution, lamps, n, queries, run_grid_illumination):
    result = run_grid_illumination(Solution, n, lamps, queries)
    result
    return (result,)


@app.cell
def _(assert_grid_illumination, expected, result):
    assert_grid_illumination(result, expected)
    return


if __name__ == "__main__":
    app.run()
