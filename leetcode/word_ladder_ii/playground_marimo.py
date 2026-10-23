import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_ladders, run_find_ladders
    from solution import Solution

    return Solution, assert_find_ladders, run_find_ladders


@app.cell
def _():
    # Example test case
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
    return begin_word, end_word, expected, word_list


@app.cell
def _(Solution, begin_word, end_word, run_find_ladders, word_list):
    result = run_find_ladders(Solution, begin_word, end_word, word_list)
    result
    return (result,)


@app.cell
def _(assert_find_ladders, expected, result):
    assert_find_ladders(result, expected)
    return


if __name__ == "__main__":
    app.run()
