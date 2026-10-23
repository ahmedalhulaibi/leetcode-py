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
    # 487. Max Consecutive Ones II

    **Medium** · Array, Dynamic Programming, Sliding Window

    Given a binary array `nums`, return the maximum number of consecutive `1`'s in the array if you can flip at most one `0`.

    **Follow up:** What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

    ## Examples

    ```
    Input: nums = [1,0,1,1,0]
    Output: 4
    Explanation:
    - If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
    - If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
    The max number of consecutive ones is 4.
    ```

    ```
    Input: nums = [1,0,1,1,0,1]
    Output: 4
    Explanation:
    - If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
    - If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
    The max number of consecutive ones is 4.
    ```

    ## Constraints

    - `1 <= nums.length <= 10^5`
    - `nums[i]` is either `0` or `1`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_max_ones(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement find_max_ones')

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
