import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_odd_number, run_largest_odd_number
    from solution import Solution

    return Solution, assert_largest_odd_number, run_largest_odd_number


@app.cell
def _():
    # Example test case
    num = "52"
    expected = "5"
    return expected, num


@app.cell
def _(Solution, num, run_largest_odd_number):
    result = run_largest_odd_number(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_largest_odd_number, expected, result):
    assert_largest_odd_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
