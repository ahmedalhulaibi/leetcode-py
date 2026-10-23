import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_word_break, run_word_break
    from solution import Solution

    return Solution, assert_word_break, run_word_break


@app.cell
def _():
    # Example test case
    s = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    expected = ["cats and dog", "cat sand dog"]
    return expected, s, word_dict


@app.cell
def _(Solution, run_word_break, s, word_dict):
    result = run_word_break(Solution, s, word_dict)
    result
    return (result,)


@app.cell
def _(assert_word_break, expected, result):
    assert_word_break(result, expected)
    return


if __name__ == "__main__":
    app.run()
