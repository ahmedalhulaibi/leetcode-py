import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minmax_gas_dist, run_minmax_gas_dist
    from solution import Solution

    return Solution, assert_minmax_gas_dist, run_minmax_gas_dist


@app.cell
def _():
    # Example test case
    stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 9
    expected = 0.5
    return expected, k, stations


@app.cell
def _(Solution, k, run_minmax_gas_dist, stations):
    result = run_minmax_gas_dist(Solution, stations, k)
    result
    return (result,)


@app.cell
def _(assert_minmax_gas_dist, expected, result):
    assert_minmax_gas_dist(result, expected)
    return


if __name__ == "__main__":
    app.run()
