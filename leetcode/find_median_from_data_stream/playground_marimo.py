import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_median_finder, run_median_finder
    from solution import MedianFinder

    return MedianFinder, assert_median_finder, run_median_finder


@app.cell
def _():
    # Example test case
    operations = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    inputs = [[], [1], [2], [], [3], []]
    expected = [None, None, None, 1.5, None, 2.0]
    return expected, inputs, operations


@app.cell
def _(MedianFinder, inputs, operations, run_median_finder):
    result, mf = run_median_finder(MedianFinder, operations, inputs)
    print(result)
    mf
    return (result,)


@app.cell
def _(assert_median_finder, expected, result):
    assert_median_finder(result, expected)
    return


if __name__ == "__main__":
    app.run()
