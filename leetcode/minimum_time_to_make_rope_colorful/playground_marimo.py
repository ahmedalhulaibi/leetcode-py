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
    # 1578. Minimum Time to Make Rope Colorful

    **Medium** · Array, String, Dynamic Programming, Greedy

    Alice has `n` balloons arranged on a rope. You are given a **0-indexed** string `colors` where `colors[i]` is the color of the `i<sup>th</sup>` balloon.

    Alice wants the rope to be **colorful**. She does not want **two consecutive balloons** to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it **colorful**. You are given a **0-indexed** integer array `neededTime` where `neededTime[i]` is the time (in seconds) that Bob needs to remove the `i<sup>th</sup>` balloon from the rope.

    Return *the **minimum time** Bob needs to make the rope **colorful***.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/12/13/ballon1.jpg)

    ```
    Input: colors = "abaac", neededTime = [1,2,3,4,5]
    Output: 3
    ```
    **Explanation:** In the above image, 'a' is blue, 'b' is red, and 'c' is green. Bob can remove the blue balloon at index 2. This takes 3 seconds. There are no longer two consecutive balloons of the same color. Total time = 3.

    ![Example 2](https://assets.leetcode.com/uploads/2021/12/13/balloon2.jpg)

    ```
    Input: colors = "abc", neededTime = [1,2,3]
    Output: 0
    ```
    **Explanation:** The rope is already colorful. Bob does not need to remove any balloons from the rope.

    ![Example 3](https://assets.leetcode.com/uploads/2021/12/13/balloon3.jpg)

    ```
    Input: colors = "aabaa", neededTime = [1,2,3,4,1]
    Output: 2
    ```
    **Explanation:** Bob will remove the balloons at indices 0 and 4. Each balloon takes 1 second to remove. There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

    ## Constraints

    - n == colors.length == neededTime.length
    - 1 <= n <= 10^5
    - 1 <= neededTime[i] <= 10^4
    - colors consists of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_cost(self, colors: str, needed_time: list[int]) -> int:
            raise NotImplementedError('Implement min_cost')

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
