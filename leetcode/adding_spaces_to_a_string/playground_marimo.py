import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_add_spaces, run_add_spaces
    from solution import Solution

    return Solution, assert_add_spaces, run_add_spaces


@app.cell
def _():
    # Example test case
    s = "LeetcodeHelpsMeLearn"
    spaces = [8, 13, 15]
    expected = "Leetcode Helps Me Learn"
    return expected, s, spaces


@app.cell
def _(Solution, run_add_spaces, s, spaces):
    result = run_add_spaces(Solution, s, spaces)
    result
    return (result,)


@app.cell
def _(assert_add_spaces, expected, result):
    assert_add_spaces(result, expected)
    return


if __name__ == "__main__":
    app.run()
