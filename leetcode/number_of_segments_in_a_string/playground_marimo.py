import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_segments, run_count_segments
    from solution import Solution

    return Solution, assert_count_segments, run_count_segments


@app.cell
def _():
    # Example test case
    s = "Hello, my name is John"
    expected = 5
    return expected, s


@app.cell
def _(Solution, run_count_segments, s):
    result = run_count_segments(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_count_segments, expected, result):
    assert_count_segments(result, expected)
    return


if __name__ == "__main__":
    app.run()
