import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_fraction_to_decimal, run_fraction_to_decimal
    from solution import Solution

    return Solution, assert_fraction_to_decimal, run_fraction_to_decimal


@app.cell
def _():
    # Example test case
    numerator = 4
    denominator = 333
    expected = "0.(012)"
    return denominator, expected, numerator


@app.cell
def _(Solution, denominator, numerator, run_fraction_to_decimal):
    result = run_fraction_to_decimal(Solution, numerator, denominator)
    result
    return (result,)


@app.cell
def _(assert_fraction_to_decimal, expected, result):
    assert_fraction_to_decimal(result, expected)
    return


if __name__ == "__main__":
    app.run()
