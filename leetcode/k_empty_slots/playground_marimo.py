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
    # 683. K Empty Slots

    **Hard** · Array, Binary Indexed Tree, Segment Tree, Queue, Ordered Set, Sliding Window, Monotonic Queue, Heap (Priority Queue)

    You have `n` bulbs in a row numbered from `1` to `n`. Initially, all the bulbs are turned off. We turn on **exactly one** bulb every day until all bulbs are on after `n` days.

    You are given an array `bulbs` of length `n` where `bulbs[i] = x` means that on the `(i+1)`-th day, we will turn on the bulb at position `x` where `i` is **0-indexed** and `x` is **1-indexed**.

    Given an integer `k`, return *the **minimum day number** such that there exists two **turned on** bulbs that have **exactly** `k` bulbs between them that are **all turned off**. If there is no such day, return `-1`.*

    ## Examples

    ```
    Input: bulbs = [1,3,2], k = 1
    Output: 2
    ```
    **Explanation:**
    - On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
    - On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
    - On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
    We return 2 because on the second day, there were two on bulbs with one off bulb between them.

    ```
    Input: bulbs = [1,2,3], k = 1
    Output: -1
    ```

    ## Constraints

    - `n == bulbs.length`
    - `1 <= n <= 2 * 10^4`
    - `1 <= bulbs[i] <= n`
    - `bulbs` is a permutation of numbers from `1` to `n`.
    - `0 <= k <= 2 * 10^4`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def k_empty_slots(self, bulbs: list[int], k: int) -> int:
            raise NotImplementedError('Implement k_empty_slots')

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
