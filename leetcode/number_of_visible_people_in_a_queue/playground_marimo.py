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
    # 1944. Number of Visible People in a Queue

    **Hard** · Array, Stack, Monotonic Stack

    There are `n` people standing in a queue, and they numbered from `0` to `n - 1` in **left to right** order. You are given an array `heights` of **distinct** integers where `heights[i]` represents the height of the `ith` person.

    A person can **see** another person to their right in the queue if everybody in between is **shorter** than both of them. More formally, the `ith` person can see the `jth` person if `i < j` and `min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1])`.

    Return *an array* `answer` *of length* `n` *where* `answer[i]` *is the **number of people** the `ith` person can **see** to their right in the queue*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/05/29/queue-plane.jpg)

    ```
    Input: heights = [10,6,8,5,11,9]
    Output: [3,1,2,1,1,0]
    ```
    **Explanation:**
    - Person 0 can see person 1, 2, and 4.
    - Person 1 can see person 2.
    - Person 2 can see person 3 and 4.
    - Person 3 can see person 4.
    - Person 4 can see person 5.
    - Person 5 can see no one since nobody is to the right of them.

    ```
    Input: heights = [5,1,2,3,10]
    Output: [4,1,1,1,0]
    ```

    ## Constraints

    - `n == heights.length`
    - `1 <= n <= 10^5`
    - `1 <= heights[i] <= 10^5`
    - All the values of `heights` are **unique**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def can_see_persons_count(self, heights: list[int]) -> list[int]:
            raise NotImplementedError('Implement can_see_persons_count')

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
