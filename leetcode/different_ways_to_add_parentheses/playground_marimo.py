import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_diff_ways_to_compute, run_diff_ways_to_compute
    from solution import Solution

    return Solution, assert_diff_ways_to_compute, run_diff_ways_to_compute


@app.cell
def _():
    # Example test case
    expression = "2-1-1"
    expected = [0, 2]
    return expected, expression


@app.cell
def _(Solution, expression, run_diff_ways_to_compute):
    result = run_diff_ways_to_compute(Solution, expression)
    result
    return (result,)


@app.cell
def _(assert_diff_ways_to_compute, expected, result):
    assert_diff_ways_to_compute(result, expected)
    return


if __name__ == "__main__":
    app.run()
