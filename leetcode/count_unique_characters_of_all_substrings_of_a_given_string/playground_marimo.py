import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_unique_letter_string, run_unique_letter_string
    from solution import Solution

    return Solution, assert_unique_letter_string, run_unique_letter_string


@app.cell
def _():
    # Example test case
    s = "ABC"
    expected = 10
    return expected, s


@app.cell
def _(Solution, run_unique_letter_string, s):
    result = run_unique_letter_string(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_unique_letter_string, expected, result):
    assert_unique_letter_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
