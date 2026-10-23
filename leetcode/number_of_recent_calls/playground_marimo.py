import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_recent_counter, run_recent_counter
    from solution import RecentCounter

    return RecentCounter, assert_recent_counter, run_recent_counter


@app.cell
def _():
    # Example test case
    operations = ["RecentCounter", "ping", "ping", "ping", "ping"]
    inputs = [[], [1], [100], [3001], [3002]]
    expected = [None, 1, 2, 3, 3]
    return expected, inputs, operations


@app.cell
def _(RecentCounter, inputs, operations, run_recent_counter):
    result, counter = run_recent_counter(RecentCounter, operations, inputs)
    print(result)
    counter
    return (result,)


@app.cell
def _(assert_recent_counter, expected, result):
    assert_recent_counter(result, expected)
    return


if __name__ == "__main__":
    app.run()
