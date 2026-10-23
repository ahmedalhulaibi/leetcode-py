import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_cost_connect_points, run_min_cost_connect_points
    from solution import Solution

    return (
        Solution,
        assert_min_cost_connect_points,
        run_min_cost_connect_points,
    )


@app.cell
def _():
    # Example test case
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    expected = 20
    return expected, points


@app.cell
def _(Solution, points, run_min_cost_connect_points):
    result = run_min_cost_connect_points(Solution, points)
    result
    return (result,)


@app.cell
def _(assert_min_cost_connect_points, expected, result):
    assert_min_cost_connect_points(result, expected)
    return


if __name__ == "__main__":
    app.run()
