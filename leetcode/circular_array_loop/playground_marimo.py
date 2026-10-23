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
    # 457. Circular Array Loop

    **Medium** · Array, Hash Table, Two Pointers, Floyd's Cycle Finding Algorithm

    You are playing a game involving a **circular** array of non-zero integers `nums`. Each `nums[i]` denotes the number of indices forward/backward you must move if you are located at index `i`:

    - If `nums[i]` is positive, move `nums[i]` steps **forward**, and
    - If `nums[i]` is negative, move `abs(nums[i])` steps **backward**.

    Since the array is **circular**, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

    A **cycle** in the array consists of a sequence of indices `seq` of length `k` where:

    - Following the movement rules above results in the repeating index sequence `seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...`
    - Every `nums[seq[j]]` is either **all positive** or **all negative**.
    - `k > 1`

    Return `true` if there is a **cycle** in `nums`, or `false` otherwise.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/09/01/img1.jpg)

    ```
    Input: nums = [2,-1,1,2,2]
    Output: true
    ```
    **Explanation:** The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
    We can see the cycle 0 -> 2 -> 3 -> 0 -> ..., and all of its nodes are white (jumping in the same direction).

    ![Example 2](https://assets.leetcode.com/uploads/2022/09/01/img2.jpg)

    ```
    Input: nums = [-1,-2,-3,-4,-5,6]
    Output: false
    ```
    **Explanation:** The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
    The only cycle is of size 1, so we return false.

    ![Example 3](https://assets.leetcode.com/uploads/2022/09/01/img3.jpg)

    ```
    Input: nums = [1,-1,5,1,4]
    Output: true
    ```
    **Explanation:** The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
    We can see the cycle 0 -> 1 -> 0 -> ..., and while it is of size > 1, it has a node jumping forward and a node jumping backward, so **it is not a cycle**.
    We can see the cycle 3 -> 4 -> 3 -> ..., and all of its nodes are white (jumping in the same direction).

    ## Constraints

    - 1 <= nums.length <= 5000
    - -1000 <= nums[i] <= 1000
    - nums[i] != 0

    **Follow up:** Could you solve it in O(n) time complexity and O(1) extra space complexity?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def circular_array_loop(self, nums: list[int]) -> bool:
            raise NotImplementedError('Implement circular_array_loop')

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
