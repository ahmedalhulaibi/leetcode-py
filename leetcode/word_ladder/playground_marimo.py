import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_ladder_length, run_ladder_length
    from solution import Solution

    return Solution, assert_ladder_length, run_ladder_length


@app.cell
def _():
    # Example test case
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected = 5
    return begin_word, end_word, expected, word_list


@app.cell
def _(Solution, begin_word, end_word, run_ladder_length, word_list):
    result = run_ladder_length(Solution, begin_word, end_word, word_list)
    result
    return (result,)


@app.cell
def _(assert_ladder_length, expected, result):
    assert_ladder_length(result, expected)
    return


if __name__ == "__main__":
    app.run()
