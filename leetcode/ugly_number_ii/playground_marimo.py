import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_nth_ugly_number, run_nth_ugly_number
    from solution import Solution

    return Solution, assert_nth_ugly_number, run_nth_ugly_number


@app.cell
def _():
    # Example test case
    n = 10
    expected = 12
    return expected, n


@app.cell
def _(Solution, n, run_nth_ugly_number):
    result = run_nth_ugly_number(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_nth_ugly_number, expected, result):
    assert_nth_ugly_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
