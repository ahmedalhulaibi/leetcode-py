import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_data_stream_as_disjoint_intervals, run_data_stream_as_disjoint_intervals
    from solution import SummaryRanges

    return (
        SummaryRanges,
        assert_data_stream_as_disjoint_intervals,
        run_data_stream_as_disjoint_intervals,
    )


@app.cell
def _():
    # Example test case
    operations = ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals"]
    inputs = [[], [1], [], [3], []]
    expected = [None, None, [[1, 1]], None, [[1, 1], [3, 3]]]
    return expected, inputs, operations


@app.cell
def _(
    SummaryRanges,
    inputs,
    operations,
    run_data_stream_as_disjoint_intervals,
):
    result = run_data_stream_as_disjoint_intervals(SummaryRanges, operations, inputs)
    result
    return (result,)


@app.cell
def _(assert_data_stream_as_disjoint_intervals, expected, result):
    assert_data_stream_as_disjoint_intervals(result, expected)
    return


if __name__ == "__main__":
    app.run()
