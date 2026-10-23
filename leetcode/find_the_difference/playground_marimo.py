import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_the_difference, run_find_the_difference
    from solution import Solution

    return Solution, assert_find_the_difference, run_find_the_difference


@app.cell
def _():
    # Example test case
    s = "abcd"
    t = "abcde"
    expected = "e"
    return expected, s, t


@app.cell
def _(Solution, run_find_the_difference, s, t):
    result = run_find_the_difference(Solution, s, t)
    result
    return (result,)


@app.cell
def _(assert_find_the_difference, expected, result):
    assert_find_the_difference(result, expected)
    return


if __name__ == "__main__":
    app.run()
