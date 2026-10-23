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
    # 2206. Divide Array Into Equal Pairs

    **Easy** · Array, Hash Table, Bit Manipulation, Counting

    You are given an integer array `nums` consisting of `2 * n` integers.

    You need to divide `nums` into `n` pairs such that:

    - Each element belongs to **exactly one** pair.
    - The elements present in a pair are **equal**.

    Return `true` if nums can be divided into `n` pairs, otherwise return `false`.

    ## Examples

    ```
    Input: nums = [3,2,3,2,2,2]
    Output: true
    Explanation:
    There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
    If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
    ```

    ```
    Input: nums = [1,2,3,4]
    Output: false
    Explanation:
    There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
    ```

    ## Constraints

    - nums.length == 2 * n
    - 1 <= n <= 500
    - 1 <= nums[i] <= 500



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def divide_array_into_equal_pairs(self, nums: list[int]) -> bool:
            raise NotImplementedError('Implement divide_array_into_equal_pairs')

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
