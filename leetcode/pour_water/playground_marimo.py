import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_pour_water, run_pour_water
    from solution import Solution

    return Solution, assert_pour_water, run_pour_water


@app.cell
def _():
    # Example test case
    heights = [2, 1, 1, 2, 1, 2, 2]
    volume = 4
    k = 3
    expected = [2, 2, 2, 3, 2, 2, 2]
    return expected, heights, k, volume


@app.cell
def _(Solution, heights, k, run_pour_water, volume):
    result = run_pour_water(Solution, heights, volume, k)
    result
    return (result,)


@app.cell
def _(assert_pour_water, expected, result):
    assert_pour_water(result, expected)
    return


if __name__ == "__main__":
    app.run()
