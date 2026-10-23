import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_earliest_acq, run_earliest_acq
    from solution import Solution

    return Solution, assert_earliest_acq, run_earliest_acq


@app.cell
def _():
    # Example test case
    logs = [
        [20190101, 0, 1],
        [20190104, 3, 4],
        [20190107, 2, 3],
        [20190211, 1, 5],
        [20190224, 2, 4],
        [20190301, 0, 3],
        [20190312, 1, 2],
        [20190322, 4, 5],
    ]
    n = 6
    expected = 20190301
    return expected, logs, n


@app.cell
def _(Solution, logs, n, run_earliest_acq):
    result = run_earliest_acq(Solution, logs, n)
    result
    return (result,)


@app.cell
def _(assert_earliest_acq, expected, result):
    assert_earliest_acq(result, expected)
    return


if __name__ == "__main__":
    app.run()
