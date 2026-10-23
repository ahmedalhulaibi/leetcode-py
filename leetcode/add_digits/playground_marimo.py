import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_add_digits, run_add_digits
    from solution import Solution

    return Solution, assert_add_digits, run_add_digits


@app.cell
def _():
    # Example test case
    num = 38
    expected = 2
    return expected, num


@app.cell
def _(Solution, num, run_add_digits):
    result = run_add_digits(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_add_digits, expected, result):
    assert_add_digits(result, expected)
    return


if __name__ == "__main__":
    app.run()
