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
    # 2161. Partition Array According to Given Pivot

    **Medium** · Array, Two Pointers, Simulation

    You are given a **0-indexed** integer array `nums` and an integer `pivot`. Rearrange `nums` such that the following conditions are satisfied:

    - Every element less than `pivot` appears **before** every element greater than `pivot`.
    - Every element equal to `pivot` appears **in between** the elements less than and greater than `pivot`.
    - The **relative order** of the elements less than `pivot` and the elements greater than `pivot` is maintained. More formally, consider every `p_i`, `p_j` where `p_i` is the new position of the `i`th element and `p_j` is the new position of the `j`th element. If `i < j` and **both** elements are smaller (or larger) than `pivot`, then `p_i < p_j`.

    Return `nums`* after the rearrangement.*

    ## Examples

    ```
    Input: nums = [9,12,5,10,14,3,10], pivot = 10
    Output: [9,5,3,10,10,12,14]
    Explanation: The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array. The elements 12 and 14 are greater than the pivot so they are on the right side of the array. The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.
    ```

    ```
    Input: nums = [-3,4,3,2], pivot = 2
    Output: [-3,2,4,3]
    Explanation: The element -3 is less than the pivot so it is on the left side of the array. The elements 4 and 3 are greater than the pivot so they are on the right side of the array. The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.
    ```

    ## Constraints

    - `1 <= nums.length <= 10^5`
    - `-10^6 <= nums[i] <= 10^6`
    - `pivot` equals to an element of `nums`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def pivot_array(self, nums: list[int], pivot: int) -> list[int]:
            raise NotImplementedError('Implement pivot_array')

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
