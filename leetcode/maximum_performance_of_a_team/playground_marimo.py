import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_performance, run_max_performance
    from solution import Solution

    return Solution, assert_max_performance, run_max_performance


@app.cell
def _():
    # Example test case
    n = 6
    speed = [2, 10, 3, 1, 5, 8]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 2
    expected = 60
    return efficiency, expected, k, n, speed


@app.cell
def _(Solution, efficiency, k, n, run_max_performance, speed):
    result = run_max_performance(Solution, n, speed, efficiency, k)
    result
    return (result,)


@app.cell
def _(assert_max_performance, expected, result):
    assert_max_performance(result, expected)
    return


if __name__ == "__main__":
    app.run()
