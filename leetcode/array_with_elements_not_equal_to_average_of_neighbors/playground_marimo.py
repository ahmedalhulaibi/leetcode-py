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
    # 1968. Array With Elements Not Equal to Average of Neighbors

    **Medium** · Array, Greedy, Sorting

    You are given a **0-indexed** array `nums` of **distinct** integers. You want to rearrange the elements in the array such that every element in the rearranged array is **not** equal to the **average** of its neighbors.

    More formally, the rearranged array should have the property such that for every `i` in the range `1 <= i < nums.length - 1`, `(nums[i-1] + nums[i+1]) / 2` is **not** equal to `nums[i]`.

    Return **any** rearrangement of `nums` that meets the requirements.

    ## Examples

    ```
    Input: nums = [1,2,3,4,5]
    Output: [1,2,4,5,3]
    Explanation: When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5. When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5. When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.
    ```

    ```
    Input: nums = [6,2,0,9,7]
    Output: [9,7,6,2,0]
    Explanation: When i=1, nums[i] = 7, and the average of its neighbors is (9+6) / 2 = 7.5. When i=2, nums[i] = 6, and the average of its neighbors is (7+2) / 2 = 4.5. When i=3, nums[i] = 2, and the average of its neighbors is (6+0) / 2 = 3. Note that the original array [6,2,0,9,7] also satisfies the conditions.
    ```

    ## Constraints

    - `3 <= nums.length <= 10^5`
    - `0 <= nums[i] <= 10^5`
    - All elements of `nums` are **distinct**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def rearrange_array(self, nums: list[int]) -> list[int]:
            raise NotImplementedError('Implement rearrange_array')

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
