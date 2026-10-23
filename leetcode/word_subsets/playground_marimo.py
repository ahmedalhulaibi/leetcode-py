import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_word_subsets, run_word_subsets
    from solution import Solution

    return Solution, assert_word_subsets, run_word_subsets


@app.cell
def _():
    # Example test case
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["e", "o"]
    expected = ["facebook", "google", "leetcode"]
    return expected, words1, words2


@app.cell
def _(Solution, run_word_subsets, words1, words2):
    result = run_word_subsets(Solution, words1, words2)
    result
    return (result,)


@app.cell
def _(assert_word_subsets, expected, result):
    assert_word_subsets(result, expected)
    return


if __name__ == "__main__":
    app.run()
