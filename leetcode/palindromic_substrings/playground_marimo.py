import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_substrings, run_count_substrings
    from solution import Solution

    return Solution, assert_count_substrings, run_count_substrings


@app.cell
def _():
    # Example test case
    s = "abc"
    expected = 3
    return expected, s


@app.cell
def _(Solution, run_count_substrings, s):
    result = run_count_substrings(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_count_substrings, expected, result):
    assert_count_substrings(result, expected)
    return


if __name__ == "__main__":
    app.run()
