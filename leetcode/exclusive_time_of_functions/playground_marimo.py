import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_exclusive_time, run_exclusive_time
    from solution import Solution

    return Solution, assert_exclusive_time, run_exclusive_time


@app.cell
def _():
    # Example test case
    n = 2
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    expected = [3, 4]
    return expected, logs, n


@app.cell
def _(Solution, logs, n, run_exclusive_time):
    result = run_exclusive_time(Solution, n, logs)
    result
    return (result,)


@app.cell
def _(assert_exclusive_time, expected, result):
    assert_exclusive_time(result, expected)
    return


if __name__ == "__main__":
    app.run()
