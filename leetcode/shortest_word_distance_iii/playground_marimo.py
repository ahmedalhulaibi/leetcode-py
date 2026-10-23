import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_word_distance_iii, run_shortest_word_distance_iii
    from solution import Solution

    return (
        Solution,
        assert_shortest_word_distance_iii,
        run_shortest_word_distance_iii,
    )


@app.cell
def _():
    # Example test case
    words_dict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "makes"
    word2 = "makes"
    expected = 3
    return expected, word1, word2, words_dict


@app.cell
def _(Solution, run_shortest_word_distance_iii, word1, word2, words_dict):
    result = run_shortest_word_distance_iii(Solution, words_dict, word1, word2)
    result
    return (result,)


@app.cell
def _(assert_shortest_word_distance_iii, expected, result):
    assert_shortest_word_distance_iii(result, expected)
    return


if __name__ == "__main__":
    app.run()
