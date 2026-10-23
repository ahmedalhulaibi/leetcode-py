import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_anagrams, run_find_anagrams
    from solution import Solution

    return Solution, assert_find_anagrams, run_find_anagrams


@app.cell
def _():
    # Example test case
    s = "cbaebabacd"
    p = "abc"
    expected = [0, 6]
    return expected, p, s


@app.cell
def _(Solution, p, run_find_anagrams, s):
    result = run_find_anagrams(Solution, s, p)
    result
    return (result,)


@app.cell
def _(assert_find_anagrams, expected, result):
    assert_find_anagrams(result, expected)
    return


if __name__ == "__main__":
    app.run()
