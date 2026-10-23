import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_most_common_word, run_most_common_word
    from solution import Solution

    return Solution, assert_most_common_word, run_most_common_word


@app.cell
def _():
    # Example test case
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    expected = "ball"
    return banned, expected, paragraph


@app.cell
def _(Solution, banned, paragraph, run_most_common_word):
    result = run_most_common_word(Solution, paragraph, banned)
    result
    return (result,)


@app.cell
def _(assert_most_common_word, expected, result):
    assert_most_common_word(result, expected)
    return


if __name__ == "__main__":
    app.run()
