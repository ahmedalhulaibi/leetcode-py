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
    # 1911. Maximum Alternating Subsequence Sum

    **Medium** · Array, Dynamic Programming

    The <strong>alternating sum</strong> of a <strong>0-indexed</strong> array is defined as the <strong>sum</strong> of the elements at <strong>even</strong> indices <strong>minus</strong> the <strong>sum</strong> of the elements at <strong>odd</strong> indices.

    <ul>
        <li>For example, the alternating sum of <code>[4,2,5,3]</code> is <code>(4 + 5) - (2 + 3) = 4</code>.</li>
    </ul>

    Given an array <code>nums</code>, return <em>the <strong>maximum alternating sum</strong> of any subsequence of </em><code>nums</code><em> (after <strong>reindexing</strong> the elements of the subsequence)</em>.

    <p>A <strong>subsequence</strong> of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, <code>[2,7,4]</code> is a subsequence of <code>[4,2,<u>3</u>,7,2,1,<u>4</u>]</code> (the underlined elements), while <code>[2,4,2]</code> is not.</p>

    ## Examples

    ```
    Input: nums = [4,2,5,3]
    Output: 7
    Explanation: It is optimal to choose the subsequence [4,2,5] with alternating sum (4 + 5) - 2 = 7.
    ```

    ```
    Input: nums = [5,6,7,8]
    Output: 8
    Explanation: It is optimal to choose the subsequence [8] with alternating sum 8.
    ```

    ```
    Input: nums = [6,2,1,2,4,5]
    Output: 10
    Explanation: It is optimal to choose the subsequence [6,1,5] with alternating sum (6 + 5) - 1 = 10.
    ```

    ## Constraints

    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_alternating_sum(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement max_alternating_sum')

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
