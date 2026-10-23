import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_substring, run_find_substring
    from solution import Solution

    return Solution, assert_find_substring, run_find_substring


@app.cell
def _():
    # Example test case
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    expected = [0, 9]
    return expected, s, words


@app.cell
def _(Solution, run_find_substring, s, words):
    result = run_find_substring(Solution, s, words)
    result
    return (result,)


@app.cell
def _(assert_find_substring, expected, result):
    assert_find_substring(result, expected)
    return


if __name__ == "__main__":
    app.run()
