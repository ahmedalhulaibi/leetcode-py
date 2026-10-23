import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_equal_substring, run_equal_substring
    from solution import Solution

    return Solution, assert_equal_substring, run_equal_substring


@app.cell
def _():
    # Example test case
    s = "abcd"
    t = "bcdf"
    max_cost = 3
    expected = 3
    return expected, max_cost, s, t


@app.cell
def _(Solution, max_cost, run_equal_substring, s, t):
    result = run_equal_substring(Solution, s, t, max_cost)
    result
    return (result,)


@app.cell
def _(assert_equal_substring, expected, result):
    assert_equal_substring(result, expected)
    return


if __name__ == "__main__":
    app.run()
