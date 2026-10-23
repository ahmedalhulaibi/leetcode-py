import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_valid_parentheses, run_longest_valid_parentheses
    from solution import Solution

    return (
        Solution,
        assert_longest_valid_parentheses,
        run_longest_valid_parentheses,
    )


@app.cell
def _():
    # Example test case
    s = ")()())"
    expected = 4
    return expected, s


@app.cell
def _(Solution, run_longest_valid_parentheses, s):
    result = run_longest_valid_parentheses(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_longest_valid_parentheses, expected, result):
    assert_longest_valid_parentheses(result, expected)
    return


if __name__ == "__main__":
    app.run()
