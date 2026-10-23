import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_extra_char, run_min_extra_char
    from solution import Solution

    return Solution, assert_min_extra_char, run_min_extra_char


@app.cell
def _():
    # Example test case
    s = "leetscode"
    dictionary = ["leet", "code", "leetcode"]
    expected = 1
    return dictionary, expected, s


@app.cell
def _(Solution, dictionary, run_min_extra_char, s):
    result = run_min_extra_char(Solution, s, dictionary)
    result
    return (result,)


@app.cell
def _(assert_min_extra_char, expected, result):
    assert_min_extra_char(result, expected)
    return


if __name__ == "__main__":
    app.run()
