import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_number_of_lines, run_number_of_lines
    from solution import Solution

    return Solution, assert_number_of_lines, run_number_of_lines


@app.cell
def _():
    # Example test case
    widths = [10] * 26
    s = "abcdefghijklmnopqrstuvwxyz"
    expected = [3, 60]
    return expected, s, widths


@app.cell
def _(Solution, run_number_of_lines, s, widths):
    result = run_number_of_lines(Solution, widths, s)
    result
    return (result,)


@app.cell
def _(assert_number_of_lines, expected, result):
    assert_number_of_lines(result, expected)
    return


if __name__ == "__main__":
    app.run()
