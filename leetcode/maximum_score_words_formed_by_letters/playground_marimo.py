import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_score_words, run_max_score_words
    from solution import Solution

    return Solution, assert_max_score_words, run_max_score_words


@app.cell
def _():
    # Example test case
    words = ["dog", "cat", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    expected = 23
    return expected, letters, score, words


@app.cell
def _(Solution, letters, run_max_score_words, score, words):
    result = run_max_score_words(Solution, words, letters, score)
    result
    return (result,)


@app.cell
def _(assert_max_score_words, expected, result):
    assert_max_score_words(result, expected)
    return


if __name__ == "__main__":
    app.run()
