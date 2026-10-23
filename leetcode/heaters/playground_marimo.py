import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_radius, run_find_radius
    from solution import Solution

    return Solution, assert_find_radius, run_find_radius


@app.cell
def _():
    # Example test case
    houses = [1, 2, 3]
    heaters = [2]
    expected = 1
    return expected, heaters, houses


@app.cell
def _(Solution, heaters, houses, run_find_radius):
    result = run_find_radius(Solution, houses, heaters)
    result
    return (result,)


@app.cell
def _(assert_find_radius, expected, result):
    assert_find_radius(result, expected)
    return


if __name__ == "__main__":
    app.run()
