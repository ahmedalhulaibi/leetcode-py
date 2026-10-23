import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_original_digits, run_original_digits
    from solution import Solution

    return Solution, assert_original_digits, run_original_digits


@app.cell
def _():
    # Example test case
    s = "owoztneoer"
    expected = "012"
    return expected, s


@app.cell
def _(Solution, run_original_digits, s):
    result = run_original_digits(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_original_digits, expected, result):
    assert_original_digits(result, expected)
    return


if __name__ == "__main__":
    app.run()
