import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_rand_point, run_rand_point
    from solution import Solution

    return Solution, assert_rand_point, run_rand_point


@app.cell
def _():
    # Example test case
    radius = 1.0
    x_center = 0.0
    y_center = 0.0
    seed = 42
    n = 20
    return n, radius, seed, x_center, y_center


@app.cell
def _(Solution, n, radius, run_rand_point, seed, x_center, y_center):
    result = run_rand_point(Solution, radius, x_center, y_center, seed, n)
    result
    return (result,)


@app.cell
def _(assert_rand_point, n, radius, result, x_center, y_center):
    assert_rand_point(result, radius, x_center, y_center, n)
    return


if __name__ == "__main__":
    app.run()
