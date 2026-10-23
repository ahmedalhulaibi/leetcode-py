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
    # 2542. Maximum Subsequence Score

    **Medium** · Array, Greedy, Sorting, Heap (Priority Queue)

    You are given two <strong>0-indexed</strong> integer arrays <code>nums1</code> and <code>nums2</code> of equal length <code>n</code> and a positive integer <code>k</code>. You must choose a <strong>subsequence</strong> of indices from <code>nums1</code> of length <code>k</code>.

    <p>For chosen indices <code>i<sub>0</sub></code>, <code>i<sub>1</sub></code>, ..., <code>i<sub>k - 1</sub></code>, your <strong>score</strong> is defined as:</p>

    <ul>
    <li>The sum of the selected elements from <code>nums1</code> multiplied with the <strong>minimum</strong> of the selected elements from <code>nums2</code>.</li>
    <li>It can defined simply as: <code>(nums1[i<sub>0</sub>] + nums1[i<sub>1</sub>] +...+ nums1[i<sub>k - 1</sub>]) * min(nums2[i<sub>0</sub>] , nums2[i<sub>1</sub>], ... ,nums2[i<sub>k - 1</sub>])</code>.</li>
    </ul>

    <p>Return <em>the <strong>maximum</strong> possible score.</em></p>

    <p>A <strong>subsequence</strong> of indices of an array is a set that can be derived from the set <code>{0, 1, ..., n-1}</code> by deleting some or no elements.</p>

    ## Examples

    ```
    Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
    Output: 12
    Explanation:
    The four possible subsequence scores are:
    - We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
    - We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6.
    - We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12.
    - We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
    Therefore, we return the max score, which is 12.
    ```

    ```
    Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
    Output: 30
    Explanation:
    Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.
    ```

    ## Constraints

    - n == nums1.length == nums2.length
    - 1 <= n <= 10^5
    - 0 <= nums1[i], nums2[j] <= 10^5
    - 1 <= k <= n



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_score(self, nums1: list[int], nums2: list[int], k: int) -> int:
            raise NotImplementedError('Implement max_score')

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
