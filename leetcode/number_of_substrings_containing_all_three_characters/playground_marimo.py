import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_number_of_substrings, run_number_of_substrings
    from solution import Solution

    return Solution, assert_number_of_substrings, run_number_of_substrings


@app.cell
def _():
    # Example test case
    s = "abcabc"
    expected = 10
    return expected, s


@app.cell
def _(Solution, run_number_of_substrings, s):
    result = run_number_of_substrings(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_number_of_substrings, expected, result):
    assert_number_of_substrings(result, expected)
    return


if __name__ == "__main__":
    app.run()
