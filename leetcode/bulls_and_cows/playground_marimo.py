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
    # 299. Bulls and Cows

    **Medium** · Hash Table, String, Counting

    You are playing the [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows) game with your friend.

    You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

    - The number of `"bulls"`, which are digits in the guess that are in the correct position.
    - The number of `"cows"`, which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

    Given the secret number `secret` and your friend's guess `guess`, return *the hint for your friend's guess*.

    The hint should be formatted as `"xAyB"`, where `x` is the number of bulls and `y` is the number of cows. Note that both `secret` and `guess` may contain duplicate digits.

    ## Examples

    ```
    Input: secret = "1807", guess = "7810"
    Output: "1A3B"
    Explanation: Bulls are connected with a '|' and cows are underlined:
    "1807"
      |
    "7810"
    ```

    ```
    Input: secret = "1123", guess = "0111"
    Output: "1A1B"
    Explanation: Bulls are connected with a '|' and cows are underlined:
    "1123"        "1123"
      |      or     |
    "0111"        "0111"
    Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
    ```

    ## Constraints

    - 1 <= secret.length, guess.length <= 1000
    - secret.length == guess.length
    - secret and guess consist of digits only.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def get_hint(self, secret: str, guess: str) -> str:
            raise NotImplementedError('Implement get_hint')

    practice_exports = {'Solution': Solution}
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
