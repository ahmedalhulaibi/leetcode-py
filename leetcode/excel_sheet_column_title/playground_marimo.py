import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_convert_to_title, run_convert_to_title
    from solution import Solution

    return Solution, assert_convert_to_title, run_convert_to_title


@app.cell
def _():
    # Example test case
    column_number = 28
    expected = "AB"
    return column_number, expected


@app.cell
def _(Solution, column_number, run_convert_to_title):
    result = run_convert_to_title(Solution, column_number)
    result
    return (result,)


@app.cell
def _(assert_convert_to_title, expected, result):
    assert_convert_to_title(result, expected)
    return


if __name__ == "__main__":
    app.run()
