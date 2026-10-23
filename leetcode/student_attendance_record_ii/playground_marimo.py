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
    n = 2
    expected = 8
    return expected, n


@app.cell
def _(Solution, n, run_check_record):
    result = run_check_record(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_check_record, expected, result):
    assert_check_record(result, expected)
    return


if __name__ == "__main__":
    app.run()
