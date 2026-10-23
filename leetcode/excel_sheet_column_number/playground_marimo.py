import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_title_to_number, run_title_to_number
    from solution import Solution

    return Solution, assert_title_to_number, run_title_to_number


@app.cell
def _():
    # Example test case
    column_title = "AB"
    expected = 28
    return column_title, expected


@app.cell
def _(Solution, column_title, run_title_to_number):
    result = run_title_to_number(Solution, column_title)
    result
    return (result,)


@app.cell
def _(assert_title_to_number, expected, result):
    assert_title_to_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
