import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_covered_intervals, run_remove_covered_intervals
    from solution import Solution

    return (
        Solution,
        assert_remove_covered_intervals,
        run_remove_covered_intervals,
    )


@app.cell
def _():
    # Example test case
    intervals = [[1, 4], [3, 6], [2, 8]]
    expected = 2
    return expected, intervals


@app.cell
def _(Solution, intervals, run_remove_covered_intervals):
    result = run_remove_covered_intervals(Solution, intervals)
    result
    return (result,)


@app.cell
def _(assert_remove_covered_intervals, expected, result):
    assert_remove_covered_intervals(result, expected)
    return


if __name__ == "__main__":
    app.run()
