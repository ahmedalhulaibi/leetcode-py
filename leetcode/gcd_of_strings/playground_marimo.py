import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_gcd_of_strings, run_gcd_of_strings
    from solution import Solution

    return Solution, assert_gcd_of_strings, run_gcd_of_strings


@app.cell
def _():
    # Example test case
    str1 = "ABCABC"
    str2 = "ABC"
    expected = "ABC"
    return expected, str1, str2


@app.cell
def _(Solution, run_gcd_of_strings, str1, str2):
    result = run_gcd_of_strings(Solution, str1, str2)
    result
    return (result,)


@app.cell
def _(assert_gcd_of_strings, expected, result):
    assert_gcd_of_strings(result, expected)
    return


if __name__ == "__main__":
    app.run()
