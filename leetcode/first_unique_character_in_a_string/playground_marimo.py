import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_first_uniq_char, run_first_uniq_char
    from solution import Solution

    return Solution, assert_first_uniq_char, run_first_uniq_char


@app.cell
def _():
    # Example test case
    s = "leetcode"
    expected = 0
    return expected, s


@app.cell
def _(Solution, run_first_uniq_char, s):
    result = run_first_uniq_char(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_first_uniq_char, expected, result):
    assert_first_uniq_char(result, expected)
    return


if __name__ == "__main__":
    app.run()
