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
    mo.md(r"""
    # 915. Partition Array into Disjoint Intervals

    **Medium** · Array

    <p>Given an integer array <code>nums</code>, partition it into two (contiguous) subarrays <code>left</code> and <code>right</code> so that:</p>

    <ul>
        <li>Every element in <code>left</code> is less than or equal to every element in <code>right</code>.</li>
        <li><code>left</code> and <code>right</code> are non-empty.</li>
        <li><code>left</code> has the smallest possible size.</li>
    </ul>

    <p>Return <em>the length of </em><code>left</code><em> after such a partitioning</em>.</p>

    <p>Test cases are generated such that partitioning exists.</p>

    ## Examples

    ```
    Input: nums = [5,0,3,8,6]
    Output: 3
    Explanation: left = [5,0,3], right = [8,6]
    ```

    ```
    Input: nums = [1,1,1,0,6,12]
    Output: 4
    Explanation: left = [1,1,1,0], right = [6,12]
    ```

    ## Constraints

    - 2 <= nums.length <= 10^5
    - 0 <= nums[i] <= 10^6
    - There is at least one valid answer for the given input.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def partition_disjoint(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement partition_disjoint')

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
