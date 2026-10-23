# /// script
# requires-python = ">=3.10"
# dependencies = ["marimo==0.25.2", "leetcode-py-sdk[practice]==0.0.0"]
# [tool.uv.sources]
# leetcode-py-sdk = { path = "../..", editable = true }
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from leetcode_py.practice import run_practice_tests

    return mo, run_practice_tests


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # 843. Guess the Word

    **Hard** · Array, Math, String, Minimax, Interactive, Game Theory

    You are given an array of unique strings `words` where `words[i]` is six letters long. One word of `words` was chosen as a secret word.

    You are also given the helper object `Master`. You may call `Master.guess(word)` where `word` is a six-letter-long string, and it must be from `words`. `Master.guess(word)` returns:

    - `-1` if `word` is not from `words`, or
    - an integer representing the number of exact matches (value and position) of your guess to the secret word.

    There is a parameter `allowedGuesses` for each test case where `allowedGuesses` is the maximum number of times you can call `Master.guess(word)`.

    For each test case, you should call `Master.guess` with the secret word without exceeding the maximum number of allowed guesses. You will get:

    - `"Either you took too many guesses, or you did not find the secret word."` if you called `Master.guess` more than `allowedGuesses` times or if you did not call `Master.guess` with the secret word, or
    - `"You guessed the secret word correctly."` if you called `Master.guess` with the secret word with the number of calls to `Master.guess` less than or equal to `allowedGuesses`.

    The test cases are generated such that you can guess the secret word with a reasonable strategy (other than using the bruteforce method).

    ## Examples

    ```
    Input: secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10
    Output: You guessed the secret word correctly.
    Explanation:
    master.guess("aaaaaa") returns -1, because "aaaaaa" is not in words.
    master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
    master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
    master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
    master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
    We made 5 calls to master.guess, and one of them was the secret, so we pass the test case.
    ```

    ```
    Input: secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10
    Output: You guessed the secret word correctly.
    Explanation: Since there are two words, you can guess both.
    ```

    ## Constraints

    - `1 <= words.length <= 100`
    - `words[i].length == 6`
    - `words[i]` consist of lowercase English letters.
    - All the strings of `words` are **unique**.
    - `secret` exists in `words`.
    - `10 <= allowedGuesses <= 30`

    **Follow up:** What is the minimum number of guesses needed to guarantee finding the secret word?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Master:

        def __init__(self, secret: str, words: list[str], allowed_guesses: int) -> None:
            self.secret = secret
            self.wordset = set(words)
            self.allowed_guesses = allowed_guesses
            self.calls = 0
            self.found = False

        def guess(self, word: str) -> int:
            self.calls += 1
            if word not in self.wordset:
                return -1
            matches = sum((a == b for a, b in zip(word, self.secret, strict=True)))
            if matches == len(self.secret):
                self.found = True
            return matches

        def outcome(self) -> bool:
            return self.found and self.calls <= self.allowed_guesses

    class Solution:

        def find_secret_word(self, words: list[str], master: Master) -> None:
            raise NotImplementedError('Implement find_secret_word')

    practice_exports = {'Master': Master, 'Solution': Solution}
    return (practice_exports,)


@app.cell(hide_code=True)
def _(mo):
    run_tests = mo.ui.run_button(label="Run tests")
    run_tests
    return (run_tests,)


@app.cell(hide_code=True)
def _(mo, practice_exports, run_practice_tests, run_tests):
    mo.stop(not run_tests.value, mo.md("Implement your solution, then run the tests."))
    test_result = run_practice_tests(mo.notebook_dir(), practice_exports)
    mo.vstack([
        mo.md(f"**{test_result.passed} passed · {test_result.failed} failed · "
              f"{test_result.skipped} skipped**"),
        mo.md("**All tests passed.**" if test_result.exit_code == 0 else "**Tests are not passing yet.**"),
        mo.accordion({"Test output": mo.plain_text(test_result.output)}),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Notes

    Record your approach, complexity, and edge cases here.
    """)
    return


if __name__ == "__main__":
    app.run()
