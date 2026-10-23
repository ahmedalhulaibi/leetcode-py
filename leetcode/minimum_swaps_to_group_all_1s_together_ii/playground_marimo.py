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
    # 2134. Minimum Swaps to Group All 1's Together II

    **Medium** · Array, Sliding Window

    A swap is defined as taking two distinct positions in an array and swapping the values in them.

    A circular array is defined as an array where we consider the first element and the last element to be adjacent.

    Given a binary circular array `nums`, return *the minimum number of swaps required to group all* `1`*'s present in the array together at any location*.

    ## Examples

    ```
    Input: nums = [0,1,0,1,1,0,0]
    Output: 1
    Explanation: Here are a few of the ways to group all the 1's together:
    [0,0,1,1,1,0,0] using 1 swap.
    [0,1,1,1,0,0,0] using 1 swap.
    [1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
    There is no way to group all 1's together with 0 swaps.
    Thus, the minimum number of swaps required is 1.
    ```

    ```
    Input: nums = [0,1,1,1,0,0,1,1,0]
    Output: 2
    Explanation: Here are a few of the ways to group all the 1's together:
    [1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
    [1,1,1,1,1,0,0,0,0] using 2 swaps.
    There is no way to group all 1's together with 0 or 1 swaps.
    Thus, the minimum number of swaps required is 2.
    ```

    ```
    Input: nums = [1,1,0,0,1]
    Output: 0
    Explanation: All the 1's are already grouped together due to the circular property of the array.
    Thus, the minimum number of swaps required is 0.
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

        def min_swaps(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement min_swaps')

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
