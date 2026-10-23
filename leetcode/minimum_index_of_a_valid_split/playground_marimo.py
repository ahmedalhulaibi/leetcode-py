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
    # 2780. Minimum Index of a Valid Split

    **Medium** · Array, Hash Table, Sorting

    An element <code>x</code> of an integer array <code>arr</code> of length <code>m</code> is <strong>dominant</strong> if <strong>more than half</strong> the elements of <code>arr</code> have a value of <code>x</code>.</p>

    <p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> of length <code>n</code> with one <strong>dominant</strong> element.</p>

    <p>You can split <code>nums</code> at an index <code>i</code> into two arrays <code>nums[0, ..., i]</code> and <code>nums[i + 1, ..., n - 1]</code>, but the split is only <strong>valid</strong> if:</p>

    <ul>
        <li><code>0 &lt;= i &lt; n - 1</code></li>
        <li><code>nums[0, ..., i]</code>, and <code>nums[i + 1, ..., n - 1]</code> have the same dominant element.</li>
    </ul>

    <p>Here, <code>nums[i, ..., j]</code> denotes the subarray of <code>nums</code> starting at index <code>i</code> and ending at index <code>j</code>, both ends being inclusive. Particularly, if <code>j &lt; i</code> then <code>nums[i, ..., j]</code> denotes an empty subarray.</p>

    <p>Return <em>the <strong>minimum</strong> index of a <strong>valid split</strong></em>. If no valid split exists, return <code>-1</code>.</p>

    ## Examples

    ```
    Input: nums = [1,2,2,2]
    Output: 2
    Explanation: We can split the array at index 2 to obtain arrays [1,2,2] and [2].
    In array [1,2,2], element 2 is dominant since it occurs twice in the array and 2 * 2 > 3.
    In array [2], element 2 is dominant since it occurs once in the array and 1 * 2 > 1.
    Both [1,2,2] and [2] have the same dominant element as nums, so this is a valid split.
    It can be shown that index 2 is the minimum index of a valid split.
    ```

    ```
    Input: nums = [2,1,3,1,1,1,7,1,2,1]
    Output: 4
    Explanation: We can split the array at index 4 to obtain arrays [2,1,3,1,1] and [1,7,1,2,1].
    In array [2,1,3,1,1], element 1 is dominant since it occurs thrice in the array and 3 * 2 > 5.
    In array [1,7,1,2,1], element 1 is dominant since it occurs thrice in the array and 3 * 2 > 5.
    Both [2,1,3,1,1] and [1,7,1,2,1] have the same dominant element as nums, so this is a valid split.
    It can be shown that index 4 is the minimum index of a valid split.
    ```

    ```
    Input: nums = [3,3,3,3,7,2,2]
    Output: -1
    Explanation: It can be shown that there is no valid split.
    ```

    ## Constraints

    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^9
    - nums has exactly one dominant element.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_index(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement minimum_index')

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
