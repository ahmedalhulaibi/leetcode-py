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
    # 1547. Minimum Cost to Cut a Stick

    **Hard** · Array, Dynamic Programming, Sorting

    Given a wooden stick of length `n` units. The stick is labelled from `0` to `n`. For example, a stick of length **6** is labelled as follows:

    ![Stick labelled 0 to 6](https://assets.leetcode.com/uploads/2020/07/21/statement.jpg)

    Given an integer array `cuts` where `cuts[i]` denotes a position you should perform a cut at.

    You should perform the cuts in order, you can change the order of the cuts as you wish.

    The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

    Return *the minimum total cost* of the cuts.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/07/23/e1.jpg)

    ```
    Input: n = 7, cuts = [1,3,4,5]
    Output: 16
    Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the following scenario:
    ![Scenario](https://assets.leetcode.com/uploads/2020/07/21/e11.jpg)
    The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6 (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
    Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).
    ```

    ```
    Input: n = 9, cuts = [5,6,1,4,2]
    Output: 22
    Explanation: If you try the given cuts ordering the cost will be 25.
    There are much ordering with total cost <= 25, for example, the order [4, 6, 5, 2, 1] has total cost = 22 which is the minimum possible.
    ```

    ## Constraints

    - 2 <= n <= 10^6
    - 1 <= cuts.length <= min(n - 1, 100)
    - 1 <= cuts[i] <= n - 1
    - All the integers in `cuts` array are **distinct**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_cost(self, n: int, cuts: list[int]) -> int:
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
