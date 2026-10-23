import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_di_string_match, run_di_string_match
    from solution import Solution

    return Solution, assert_di_string_match, run_di_string_match


@app.cell
def _():
    # Example test case
    s = "IDID"
    expected = [0, 4, 1, 3, 2]
    return expected, s


@app.cell
def _(Solution, run_di_string_match, s):
    result = run_di_string_match(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_di_string_match, expected, result, s):
    assert_di_string_match(result, expected, s)
    return


if __name__ == "__main__":
    app.run()
