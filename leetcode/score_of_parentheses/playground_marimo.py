import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_score_of_parentheses, run_score_of_parentheses
    from solution import Solution

    return Solution, assert_score_of_parentheses, run_score_of_parentheses


@app.cell
def _():
    # Example test case
    s = "(()(()))"
    expected = 6
    return expected, s


@app.cell
def _(Solution, run_score_of_parentheses, s):
    result = run_score_of_parentheses(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_score_of_parentheses, expected, result):
    assert_score_of_parentheses(result, expected)
    return


if __name__ == "__main__":
    app.run()
