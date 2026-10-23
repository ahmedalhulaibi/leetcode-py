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
    # 2460. Apply Operations to an Array

    **Easy** · Array, Two Pointers, Simulation

    You are given a **0-indexed** array `nums` of size `n` consisting of **non-negative** integers.

    You need to apply `n - 1` operations to this array where, in the `i<sup>th</sup>` operation (**0-indexed**), you will apply the following on the `i<sup>th</sup>` element of `nums`:

    - If `nums[i] == nums[i + 1]`, then multiply `nums[i]` by `2` and set `nums[i + 1]` to `0`. Otherwise, you skip this operation.

    After performing **all** the operations, **shift** all the `0`'s to the **end** of the array.

    - For example, the array `[1,0,2,0,0,1]` after shifting all its `0`'s to the end, is `[1,2,1,0,0,0]`.

    Return *the resulting array*.

    **Note** that the operations are applied **sequentially**, not all at once.

    ## Examples

    ```
    Input: nums = [1,2,2,1,1,0]
    Output: [1,4,2,0,0,0]
    Explanation: We do the following operations:
    - i = 0: nums[0] and nums[1] are not equal, so we skip this operation.
    - i = 1: nums[1] and nums[2] are equal, we multiply nums[1] by 2 and change nums[2] to 0. The array becomes [1,4,0,1,1,0].
    - i = 2: nums[2] and nums[3] are not equal, so we skip this operation.
    - i = 3: nums[3] and nums[4] are equal, we multiply nums[3] by 2 and change nums[4] to 0. The array becomes [1,4,0,2,0,0].
    - i = 4: nums[4] and nums[5] are equal, we multiply nums[4] by 2 and change nums[5] to 0. The array becomes [1,4,0,2,0,0].
    After that, we shift the 0's to the end, which gives the array [1,4,2,0,0,0].
    ```

    ```
    Input: nums = [0,1]
    Output: [1,0]
    Explanation: No operation can be applied, we just shift the 0 to the end.
    ```

    ## Constraints

    - 2 <= nums.length <= 2000
    - 0 <= nums[i] <= 1000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def apply_operations(self, nums: list[int]) -> list[int]:
            raise NotImplementedError('Implement apply_operations')

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
