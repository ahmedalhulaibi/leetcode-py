import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sequential_digits, run_sequential_digits
    from solution import Solution

    return Solution, assert_sequential_digits, run_sequential_digits


@app.cell
def _():
    # Example test case
    low = 100
    high = 300
    expected = [123, 234]
    return expected, high, low


@app.cell
def _(Solution, high, low, run_sequential_digits):
    result = run_sequential_digits(Solution, low, high)
    result
    return (result,)


@app.cell
def _(assert_sequential_digits, expected, result):
    assert_sequential_digits(result, expected)
    return


if __name__ == "__main__":
    app.run()
