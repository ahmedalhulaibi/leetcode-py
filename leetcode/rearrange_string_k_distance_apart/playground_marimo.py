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
    # 358. Rearrange String k Distance Apart

    **Hard** · Greedy, Hash Table, String, Counting, Sorting, Heap (Priority Queue)

    Given a string `s` and an integer `k`, rearrange `s` such that the same characters are **at least** distance `k` from each other. If it is not possible to rearrange the string, return an empty string `"\"`.

    ## Examples

    ```
    Input: s = "aabbcc", k = 3
    Output: "abcabc"
    Explanation: The same letters are at least a distance of 3 from each other.
    ```

    ```
    Input: s = "aaabc", k = 3
    Output: "\"
    Explanation: It is not possible to rearrange the string.
    ```

    ```
    Input: s = "aaadbbcc", k = 2
    Output: "abacabcd"
    Explanation: The same letters are at least a distance of 2 from each other.
    ```

    ## Constraints

    - `1 <= s.length <= 3 * 10^5`
    - `s` consists of only lowercase English letters.
    - `0 <= k <= s.length`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import Counter, deque
    from heapq import heapify, heappop, heappush

    class Solution:

        def rearrange_string(self, s: str, k: int) -> str:
            raise NotImplementedError('Implement rearrange_string')

    practice_exports = {'Counter': Counter, 'deque': deque, 'heapify': heapify, 'heappop': heappop, 'heappush': heappush, 'Solution': Solution}
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
