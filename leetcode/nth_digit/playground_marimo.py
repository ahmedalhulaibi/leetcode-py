import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_nth_digit, run_find_nth_digit
    from solution import Solution

    return Solution, assert_find_nth_digit, run_find_nth_digit


@app.cell
def _():
    # Example test case
    n = 11
    expected = 0
    return expected, n


@app.cell
def _(Solution, n, run_find_nth_digit):
    result = run_find_nth_digit(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_find_nth_digit, expected, result):
    assert_find_nth_digit(result, expected)
    return


if __name__ == "__main__":
    app.run()
