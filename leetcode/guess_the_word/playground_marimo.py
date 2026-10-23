import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_secret_word, run_find_secret_word
    from solution import Solution

    return Solution, assert_find_secret_word, run_find_secret_word


@app.cell
def _():
    # Example test case
    secret = "acckzz"
    words = ["acckzz", "ccbazz", "eiowzz", "abcczz"]
    allowed_guesses = 10
    expected = True
    return allowed_guesses, expected, secret, words


@app.cell
def _(Solution, allowed_guesses, run_find_secret_word, secret, words):
    result = run_find_secret_word(Solution, secret, words, allowed_guesses)
    result
    return (result,)


@app.cell
def _(assert_find_secret_word, expected, result):
    assert_find_secret_word(result, expected)
    return


if __name__ == "__main__":
    app.run()
