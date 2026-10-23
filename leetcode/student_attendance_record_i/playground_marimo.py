import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_check_record, run_check_record
    from solution import Solution

    return Solution, assert_check_record, run_check_record


@app.cell
def _():
    # Example test case
    s = "PPALLP"
    expected = True
    return expected, s


@app.cell
def _(Solution, run_check_record, s):
    result = run_check_record(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_check_record, expected, result):
    assert_check_record(result, expected)
    return


if __name__ == "__main__":
    app.run()
