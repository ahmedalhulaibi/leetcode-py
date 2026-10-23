import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_generate_parenthesis, run_generate_parenthesis
    from solution import Solution

    return Solution, assert_generate_parenthesis, run_generate_parenthesis


@app.cell
def _():
    # Example test case
    n = 3
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    return expected, n


@app.cell
def _(Solution, n, run_generate_parenthesis):
    result = run_generate_parenthesis(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_generate_parenthesis, expected, result):
    assert_generate_parenthesis(result, expected)
    return


if __name__ == "__main__":
    app.run()
