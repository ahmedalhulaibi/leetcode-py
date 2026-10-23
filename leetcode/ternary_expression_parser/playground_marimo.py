import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_parse_ternary, run_parse_ternary
    from solution import Solution

    return Solution, assert_parse_ternary, run_parse_ternary


@app.cell
def _():
    # Example test case
    expression = "T?2:3"
    expected = "2"
    return expected, expression


@app.cell
def _(Solution, expression, run_parse_ternary):
    result = run_parse_ternary(Solution, expression)
    result
    return (result,)


@app.cell
def _(assert_parse_ternary, expected, result):
    assert_parse_ternary(result, expected)
    return


if __name__ == "__main__":
    app.run()
