import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_repeated_string_match, run_repeated_string_match
    from solution import Solution

    return Solution, assert_repeated_string_match, run_repeated_string_match


@app.cell
def _():
    # Example test case
    a = "abcd"
    b = "cdabcdab"
    expected = 3
    return a, b, expected


@app.cell
def _(Solution, a, b, run_repeated_string_match):
    result = run_repeated_string_match(Solution, a, b)
    result
    return (result,)


@app.cell
def _(assert_repeated_string_match, expected, result):
    assert_repeated_string_match(result, expected)
    return


if __name__ == "__main__":
    app.run()
