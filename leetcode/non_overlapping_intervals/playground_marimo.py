import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_erase_overlap_intervals, run_erase_overlap_intervals
    from solution import Solution

    return (
        Solution,
        assert_erase_overlap_intervals,
        run_erase_overlap_intervals,
    )


@app.cell
def _():
    # Example test case
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    expected = 1
    return expected, intervals


@app.cell
def _(Solution, intervals, run_erase_overlap_intervals):
    result = run_erase_overlap_intervals(Solution, intervals)
    result
    return (result,)


@app.cell
def _(assert_erase_overlap_intervals, expected, result):
    assert_erase_overlap_intervals(result, expected)
    return


if __name__ == "__main__":
    app.run()
