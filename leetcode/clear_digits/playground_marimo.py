import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_clear_digits, run_clear_digits
    from solution import Solution

    return Solution, assert_clear_digits, run_clear_digits


@app.cell
def _():
    # Example test case
    s = "cb34"
    expected = ""
    return expected, s


@app.cell
def _(Solution, run_clear_digits, s):
    result = run_clear_digits(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_clear_digits, expected, result):
    assert_clear_digits(result, expected)
    return


if __name__ == "__main__":
    app.run()
