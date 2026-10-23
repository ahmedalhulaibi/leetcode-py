import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_range_bitwise_and, run_range_bitwise_and
    from solution import Solution

    return Solution, assert_range_bitwise_and, run_range_bitwise_and


@app.cell
def _():
    # Example test case
    left = 5
    right = 7
    expected = 4
    return expected, left, right


@app.cell
def _(Solution, left, right, run_range_bitwise_and):
    result = run_range_bitwise_and(Solution, left, right)
    result
    return (result,)


@app.cell
def _(assert_range_bitwise_and, expected, result):
    assert_range_bitwise_and(result, expected)
    return


if __name__ == "__main__":
    app.run()
