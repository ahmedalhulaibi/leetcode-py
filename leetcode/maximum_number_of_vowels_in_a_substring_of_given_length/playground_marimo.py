import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_vowels, run_max_vowels
    from solution import Solution

    return Solution, assert_max_vowels, run_max_vowels


@app.cell
def _():
    # Example test case
    s = "abciiidef"
    k = 3
    expected = 3
    return expected, k, s


@app.cell
def _(Solution, k, run_max_vowels, s):
    result = run_max_vowels(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_max_vowels, expected, result):
    assert_max_vowels(result, expected)
    return


if __name__ == "__main__":
    app.run()
