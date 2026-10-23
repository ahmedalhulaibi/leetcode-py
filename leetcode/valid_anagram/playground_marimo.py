import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_anagram, run_is_anagram
    from solution import Solution

    return Solution, assert_is_anagram, run_is_anagram


@app.cell
def _():
    # Example test case
    s = "anagram"
    t = "nagaram"
    expected = True
    return expected, s, t


@app.cell
def _(Solution, run_is_anagram, s, t):
    result = run_is_anagram(Solution, s, t)
    result
    return (result,)


@app.cell
def _(assert_is_anagram, expected, result):
    assert_is_anagram(result, expected)
    return


if __name__ == "__main__":
    app.run()
