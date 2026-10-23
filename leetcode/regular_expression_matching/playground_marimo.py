import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_match, run_is_match
    from solution import Solution

    return Solution, assert_is_match, run_is_match


@app.cell
def _():
    # Example test case
    s = "aa"
    p = "a*"
    expected = True
    return expected, p, s


@app.cell
def _(Solution, p, run_is_match, s):
    result = run_is_match(Solution, s, p)
    result
    return (result,)


@app.cell
def _(assert_is_match, expected, result):
    assert_is_match(result, expected)
    return


if __name__ == "__main__":
    app.run()
