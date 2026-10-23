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
    # 1167. Minimum Cost to Connect Sticks

    **Easy** · Array, Greedy, Heap (Priority Queue)

    You have some number of sticks with positive integer lengths. These lengths are given as an array `sticks`, where `sticks[i]` is the length of the `i<sup>th</sup>` stick.

    You can connect any two sticks of lengths `x` and `y` into one stick by paying a cost of `x + y`. You must connect all the sticks until there is only one stick remaining.

    Return _the minimum cost of connecting all the given sticks into one stick in this way_.

    ## Examples

    ```
    Input: sticks = [2,4,3]
    Output: 14
    Explanation: You start with sticks = [2,4,3].
    1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
    2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
    There is only one stick left, so you are done. The total cost is 5 + 9 = 14.
    ```

    ```
    Input: sticks = [1,8,3,5]
    Output: 30
    Explanation: You start with sticks = [1,8,3,5].
    1. Combine sticks 1 and 3 for a cost of 1 + 3 = 4. Now you have sticks = [4,8,5].
    2. Combine sticks 4 and 5 for a cost of 4 + 5 = 9. Now you have sticks = [9,8].
    3. Combine sticks 9 and 8 for a cost of 9 + 8 = 17. Now you have sticks = [17].
    There is only one stick left, so you are done. The total cost is 4 + 9 + 17 = 30.
    ```

    ```
    Input: sticks = [5]
    Output: 0
    Explanation: There is only one stick, so you don't need to do anything. The total cost is 0.
    ```

    ## Constraints

    - 1 <= sticks.length <= 10^4
    - 1 <= sticks[i] <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def connect_sticks(self, sticks: list[int]) -> int:
            raise NotImplementedError('Implement connect_sticks')

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
