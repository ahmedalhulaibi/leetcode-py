import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_parse_bool_expr, run_parse_bool_expr
    from solution import Solution

    return Solution, assert_parse_bool_expr, run_parse_bool_expr


@app.cell
def _():
    # Example test case
    expression = "|(f, f, f, t)"
    expected = True
    return expected, expression


@app.cell
def _(Solution, expression, run_parse_bool_expr):
    result = run_parse_bool_expr(Solution, expression)
    result
    return (result,)


@app.cell
def _(assert_parse_bool_expr, expected, result):
    assert_parse_bool_expr(result, expected)
    return


if __name__ == "__main__":
    app.run()
