import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_least_interval, run_least_interval
    from solution import Solution

    return Solution, assert_least_interval, run_least_interval


@app.cell
def _():
    # Example test case
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    expected = 8
    return expected, n, tasks


@app.cell
def _(Solution, n, run_least_interval, tasks):
    result = run_least_interval(Solution, tasks, n)
    result
    return (result,)


@app.cell
def _(assert_least_interval, expected, result):
    assert_least_interval(result, expected)
    return


if __name__ == "__main__":
    app.run()
