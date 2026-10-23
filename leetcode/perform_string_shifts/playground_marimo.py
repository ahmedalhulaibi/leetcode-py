import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_string_shift, run_string_shift
    from solution import Solution

    return Solution, assert_string_shift, run_string_shift


@app.cell
def _():
    # Example test case
    s = "abc"
    shift = [[0, 1], [1, 2]]
    expected = "cab"
    return expected, s, shift


@app.cell
def _(Solution, run_string_shift, s, shift):
    result = run_string_shift(Solution, s, shift)
    result
    return (result,)


@app.cell
def _(assert_string_shift, expected, result):
    assert_string_shift(result, expected)
    return


if __name__ == "__main__":
    app.run()
