import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reverse_vowels, run_reverse_vowels
    from solution import Solution

    return Solution, assert_reverse_vowels, run_reverse_vowels


@app.cell
def _():
    # Example test case
    s = "IceCreAm"
    expected = "AceCreIm"
    return expected, s


@app.cell
def _(Solution, run_reverse_vowels, s):
    result = run_reverse_vowels(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_reverse_vowels, expected, result):
    assert_reverse_vowels(result, expected)
    return


if __name__ == "__main__":
    app.run()
