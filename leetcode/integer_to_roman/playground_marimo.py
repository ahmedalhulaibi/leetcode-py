import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_int_to_roman, run_int_to_roman
    from solution import Solution

    return Solution, assert_int_to_roman, run_int_to_roman


@app.cell
def _():
    # Example test case
    num = 3749
    expected = "MMMDCCXLIX"
    return expected, num


@app.cell
def _(Solution, num, run_int_to_roman):
    result = run_int_to_roman(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_int_to_roman, expected, result):
    assert_int_to_roman(result, expected)
    return


if __name__ == "__main__":
    app.run()
