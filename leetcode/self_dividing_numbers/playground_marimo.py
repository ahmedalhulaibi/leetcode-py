import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_self_dividing_numbers, run_self_dividing_numbers
    from solution import Solution

    return Solution, assert_self_dividing_numbers, run_self_dividing_numbers


@app.cell
def _():
    # Example test case
    left = 1
    right = 22
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    return expected, left, right


@app.cell
def _(Solution, left, right, run_self_dividing_numbers):
    result = run_self_dividing_numbers(Solution, left, right)
    result
    return (result,)


@app.cell
def _(assert_self_dividing_numbers, expected, result):
    assert_self_dividing_numbers(result, expected)
    return


if __name__ == "__main__":
    app.run()
