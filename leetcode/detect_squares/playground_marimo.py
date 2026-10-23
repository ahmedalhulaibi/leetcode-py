import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_detect_squares, run_detect_squares
    from solution import DetectSquares

    return DetectSquares, assert_detect_squares, run_detect_squares


@app.cell
def _():
    # Example test case
    operations = ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
    inputs = [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
    expected = [None, None, None, None, 1, 0, None, 2]
    return expected, inputs, operations


@app.cell
def _(DetectSquares, inputs, operations, run_detect_squares):
    result = run_detect_squares(DetectSquares, operations, inputs)
    result
    return (result,)


@app.cell
def _(assert_detect_squares, expected, result):
    assert_detect_squares(result, expected)
    return


if __name__ == "__main__":
    app.run()
