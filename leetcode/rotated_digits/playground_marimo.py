import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_rotated_digits, run_rotated_digits
    from solution import Solution

    return Solution, assert_rotated_digits, run_rotated_digits


@app.cell
def _():
    # Example test case
    n = 10
    expected = 4
    return expected, n


@app.cell
def _(Solution, n, run_rotated_digits):
    result = run_rotated_digits(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_rotated_digits, expected, result):
    assert_rotated_digits(result, expected)
    return


if __name__ == "__main__":
    app.run()
