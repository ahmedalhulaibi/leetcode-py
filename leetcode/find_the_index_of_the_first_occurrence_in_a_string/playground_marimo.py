import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_str_str, run_str_str
    from solution import Solution

    return Solution, assert_str_str, run_str_str


@app.cell
def _():
    # Example test case
    haystack = "sadbutsad"
    needle = "sad"
    expected = 0
    return expected, haystack, needle


@app.cell
def _(Solution, haystack, needle, run_str_str):
    result = run_str_str(Solution, haystack, needle)
    result
    return (result,)


@app.cell
def _(assert_str_str, expected, result):
    assert_str_str(result, expected)
    return


if __name__ == "__main__":
    app.run()
