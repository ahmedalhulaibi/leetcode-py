import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_good_strings, run_count_good_strings
    from solution import Solution

    return Solution, assert_count_good_strings, run_count_good_strings


@app.cell
def _():
    # Example test case
    low = 3
    high = 3
    zero = 1
    one = 1
    expected = 8
    return expected, high, low, one, zero


@app.cell
def _(Solution, high, low, one, run_count_good_strings, zero):
    result = run_count_good_strings(Solution, low, high, zero, one)
    result
    return (result,)


@app.cell
def _(assert_count_good_strings, expected, result):
    assert_count_good_strings(result, expected)
    return


if __name__ == "__main__":
    app.run()
