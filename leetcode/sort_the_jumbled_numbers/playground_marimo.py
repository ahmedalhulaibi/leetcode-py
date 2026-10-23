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
    # 2191. Sort the Jumbled Numbers

    **Medium** · Array, Sorting

    You are given a <strong>0-indexed</strong> integer array <code>mapping</code> which represents the mapping rule of a shuffled decimal system. <code>mapping[i] = j</code> means digit <code>i</code> should be mapped to digit <code>j</code> in this system.

    The <strong>mapped value</strong> of an integer is the new integer obtained by replacing each occurrence of digit <code>i</code> in the integer with <code>mapping[i]</code> for all <code>0 &lt;= i &lt;= 9</code>.

    You are also given another integer array <code>nums</code>. Return <em>the array </em><code>nums</code><em> sorted in <strong>non-decreasing</strong> order based on the <strong>mapped values</strong> of its elements.</em>

    <p><strong>Notes:</strong></p>

    <ul>
        <li>Elements with the same mapped values should appear in the <strong>same relative order</strong> as in the input.</li>
        <li>The elements of <code>nums</code> should only be sorted based on their mapped values and <strong>not be replaced</strong> by them.</li>
    </ul>

    ## Examples

    ```
    Input: mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]
    Output: [338,38,991]
    Explanation:
    Map the number 991 as follows:
    1. mapping[9] = 6, so all occurrences of the digit 9 will become 6.
    2. mapping[1] = 9, so all occurrences of the digit 1 will become 9.
    Therefore, the mapped value of 991 is 669.
    338 maps to 007, or 7 after removing the leading zeros.
    38 maps to 07, which is also 7 after removing leading zeros.
    Since 338 and 38 share the same mapped value, they should remain in the same relative order, so 338 comes before 38.
    Thus, the sorted array is [338,38,991].
    ```

    ```
    Input: mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123]
    Output: [123,456,789]
    Explanation: 789 maps to 789, 456 maps to 456, and 123 maps to 123. Thus, the sorted array is [123,456,789].
    ```

    ## Constraints

    - mapping.length == 10
    - 0 <= mapping[i] <= 9
    - All the values of mapping[i] are unique.
    - 1 <= nums.length <= 3 * 10^4
    - 0 <= nums[i] < 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def sort_jumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
            raise NotImplementedError('Implement sort_jumbled')

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
