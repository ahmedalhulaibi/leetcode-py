import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_invalid_parentheses, run_remove_invalid_parentheses
    from solution import Solution

    return (
        Solution,
        assert_remove_invalid_parentheses,
        run_remove_invalid_parentheses,
    )


@app.cell
def _():
    # Example test case
    s = "()())()"
    expected = ["(())()", "()()()"]
    return expected, s


@app.cell
def _(Solution, run_remove_invalid_parentheses, s):
    result = run_remove_invalid_parentheses(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_remove_invalid_parentheses, expected, result):
    assert_remove_invalid_parentheses(result, expected)
    return


if __name__ == "__main__":
    app.run()
