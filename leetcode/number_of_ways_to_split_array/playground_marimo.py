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
    # 2270. Number of Ways to Split Array

    **Medium** · Array, Prefix Sum

    You are given a <strong>0-indexed</strong> integer array <code>nums</code> of length <code>n</code>.

    <p><code>nums</code> contains a <strong>valid split</strong> at index <code>i</code> if the following are true:</p>

    <ul>
        <li>The sum of the first <code>i + 1</code> elements is <strong>greater than or equal to</strong> the sum of the last <code>n - i - 1</code> elements.</li>
        <li>There is <strong>at least one</strong> element to the right of <code>i</code>. That is, <code>0 &lt;= i &lt; n - 1</code>.</li>
    </ul>

    <p>Return <em>the number of <strong>valid splits</strong> in</em> <code>nums</code>.</p>

    ## Examples

    ```
    Input: nums = [10,4,-8,7]
    Output: 2
    Explanation:
    There are three ways of splitting nums into two non-empty parts:
    - Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
    - Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
    - Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
    Thus, the number of valid splits in nums is 2.
    ```

    ```
    Input: nums = [2,3,1,0]
    Output: 2
    Explanation:
    There are two valid splits in nums:
    - Split nums at index 1. Then, the first part is [2,3], and its sum is 5. The second part is [1,0], and its sum is 1. Since 5 >= 1, i = 1 is a valid split.
    - Split nums at index 2. Then, the first part is [2,3,1], and its sum is 6. The second part is [0], and its sum is 0. Since 6 >= 0, i = 2 is a valid split.
    ```

    ## Constraints

    - 2 <= nums.length <= 10^5
    - -10^5 <= nums[i] <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def ways_to_split_array(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement ways_to_split_array')

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
