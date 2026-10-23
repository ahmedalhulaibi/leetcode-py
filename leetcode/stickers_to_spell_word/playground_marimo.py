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
    # 691. Stickers to Spell Word

    **Hard** · Array, String, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask

    We are given `n` different types of stickers. Each sticker has a lowercase English word on it.

    You would like to spell out the given string `target` by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

    Return the minimum number of stickers that you need to spell out `target`. If the task is impossible, return `-1`.

    Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

    ## Examples

    ```
    Input: stickers = ["with","example","science"], target = "thehat"
    Output: 3
    Explanation: We can use 2 "with" stickers, and 1 "example" sticker.
    After cutting and rearrange the letters of those stickers, we can form the target "thehat".
    Also, this is the minimum number of stickers necessary to form the target string.
    ```

    ```
    Input: stickers = ["notice","possible"], target = "basicbasic"
    Output: -1
    Explanation: We cannot form the target "basicbasic" from cutting letters from the given stickers.
    ```

    ## Constraints

    - n == stickers.length
    - 1 <= n <= 50
    - 1 <= stickers[i].length <= 10
    - 1 <= target.length <= 15
    - stickers[i] and target consist of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from functools import lru_cache

    class Solution:

        def min_stickers(self, stickers: list[str], target: str) -> int:
            raise NotImplementedError('Implement min_stickers')

    practice_exports = {'lru_cache': lru_cache, 'Solution': Solution}
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
