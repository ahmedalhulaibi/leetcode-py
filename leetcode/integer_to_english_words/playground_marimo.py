import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_number_to_words, run_number_to_words
    from solution import Solution

    return Solution, assert_number_to_words, run_number_to_words


@app.cell
def _():
    # Example test case
    num = 1234567
    expected = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    return expected, num


@app.cell
def _(Solution, num, run_number_to_words):
    result = run_number_to_words(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_number_to_words, expected, result):
    assert_number_to_words(result, expected)
    return


if __name__ == "__main__":
    app.run()
