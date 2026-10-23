import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_network_delay_time, run_network_delay_time
    from solution import Solution

    return Solution, assert_network_delay_time, run_network_delay_time


@app.cell
def _():
    # Example test case
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    expected = 2
    return expected, k, n, times


@app.cell
def _(Solution, k, n, run_network_delay_time, times):
    result = run_network_delay_time(Solution, times, n, k)
    result
    return (result,)


@app.cell
def _(assert_network_delay_time, expected, result):
    assert_network_delay_time(result, expected)
    return


if __name__ == "__main__":
    app.run()
