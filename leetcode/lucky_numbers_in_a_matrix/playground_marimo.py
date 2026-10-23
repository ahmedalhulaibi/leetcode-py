import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_lucky_numbers, run_lucky_numbers
    from solution import Solution

    return Solution, assert_lucky_numbers, run_lucky_numbers


@app.cell
def _():
    # Example test case
    matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    expected = [15]
    return expected, matrix


@app.cell
def _(Solution, matrix, run_lucky_numbers):
    result = run_lucky_numbers(Solution, matrix)
    result
    return (result,)


@app.cell
def _(assert_lucky_numbers, expected, result):
    assert_lucky_numbers(result, expected)
    return


if __name__ == "__main__":
    app.run()
