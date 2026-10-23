import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import (
        assert_find_all_concatenated_words_in_a_dict,
        run_find_all_concatenated_words_in_a_dict,
    )
    from solution import Solution

    return (
        Solution,
        assert_find_all_concatenated_words_in_a_dict,
        run_find_all_concatenated_words_in_a_dict,
    )


@app.cell
def _():
    # Example test case
    words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    expected = ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
    return expected, words


@app.cell
def _(Solution, run_find_all_concatenated_words_in_a_dict, words):
    result = run_find_all_concatenated_words_in_a_dict(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_find_all_concatenated_words_in_a_dict, expected, result):
    assert_find_all_concatenated_words_in_a_dict(result, expected)
    return


if __name__ == "__main__":
    app.run()
