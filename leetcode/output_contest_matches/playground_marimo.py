import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_contest_match, run_find_contest_match
    from solution import Solution

    return Solution, assert_find_contest_match, run_find_contest_match


@app.cell
def _():
    # Example test case
    n = 8
    expected = "(((1,8),(4,5)),((2,7),(3,6)))"
    return expected, n


@app.cell
def _(Solution, n, run_find_contest_match):
    result = run_find_contest_match(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_find_contest_match, expected, n, result):
    assert_find_contest_match(result, n, expected)
    return


if __name__ == "__main__":
    app.run()
