import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reverse_parentheses, run_reverse_parentheses
    from solution import Solution

    return Solution, assert_reverse_parentheses, run_reverse_parentheses


@app.cell
def _():
    # Example test case
    s = "(u(love)i)"
    expected = "iloveu"
    return expected, s


@app.cell
def _(Solution, run_reverse_parentheses, s):
    result = run_reverse_parentheses(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_reverse_parentheses, expected, result):
    assert_reverse_parentheses(result, expected)
    return


if __name__ == "__main__":
    app.run()
