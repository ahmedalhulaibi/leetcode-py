import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_divide, run_divide
    from solution import Solution

    return Solution, assert_divide, run_divide


@app.cell
def _():
    # Example test case
    dividend = 10
    divisor = 3
    expected = 3
    return dividend, divisor, expected


@app.cell
def _(Solution, dividend, divisor, run_divide):
    result = run_divide(Solution, dividend, divisor)
    result
    return (result,)


@app.cell
def _(assert_divide, expected, result):
    assert_divide(result, expected)
    return


if __name__ == "__main__":
    app.run()
