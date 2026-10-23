import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_confusing_number, run_confusing_number
    from solution import Solution

    return Solution, assert_confusing_number, run_confusing_number


@app.cell
def _():
    # Example test case
    n = 89
    expected = True
    return expected, n


@app.cell
def _(Solution, n, run_confusing_number):
    result = run_confusing_number(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_confusing_number, expected, result):
    assert_confusing_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
