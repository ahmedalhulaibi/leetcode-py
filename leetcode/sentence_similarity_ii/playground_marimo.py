import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_are_sentences_similar_two, run_are_sentences_similar_two
    from solution import Solution

    return (
        Solution,
        assert_are_sentences_similar_two,
        run_are_sentences_similar_two,
    )


@app.cell
def _():
    # Example test case
    sentence1 = ["great", "acting", "skills"]
    sentence2 = ["fine", "drama", "talent"]
    similar_pairs = [["great", "good"], ["fine", "good"], ["drama", "acting"], ["skills", "talent"]]
    expected = True
    return expected, sentence1, sentence2, similar_pairs


@app.cell
def _(
    Solution,
    run_are_sentences_similar_two,
    sentence1,
    sentence2,
    similar_pairs,
):
    result = run_are_sentences_similar_two(Solution, sentence1, sentence2, similar_pairs)
    result
    return (result,)


@app.cell
def _(assert_are_sentences_similar_two, expected, result):
    assert_are_sentences_similar_two(result, expected)
    return


if __name__ == "__main__":
    app.run()
