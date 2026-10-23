import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_longest_word, run_find_longest_word
    from solution import Solution

    return Solution, assert_find_longest_word, run_find_longest_word


@app.cell
def _():
    # Example test case
    s = "abpcplea"
    dictionary = ["ale", "apple", "monkey", "plea"]
    expected = "apple"
    return dictionary, expected, s


@app.cell
def _(Solution, dictionary, run_find_longest_word, s):
    result = run_find_longest_word(Solution, s, dictionary)
    result
    return (result,)


@app.cell
def _(assert_find_longest_word, expected, result):
    assert_find_longest_word(result, expected)
    return


if __name__ == "__main__":
    app.run()
