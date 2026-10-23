import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_check_valid_string, run_check_valid_string
    from solution import Solution

    return Solution, assert_check_valid_string, run_check_valid_string


@app.cell
def _():
    # Example test case
    s = "(*)"
    expected = True
    return expected, s


@app.cell
def _(Solution, run_check_valid_string, s):
    result = run_check_valid_string(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_check_valid_string, expected, result):
    assert_check_valid_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
