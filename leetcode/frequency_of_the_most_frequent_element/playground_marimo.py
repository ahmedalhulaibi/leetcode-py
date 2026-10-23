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
    # 1838. Frequency of the Most Frequent Element

    **Medium** · Array, Binary Search, Greedy, Sliding Window, Sorting, Prefix Sum

    The **frequency** of an element is the number of times it occurs in an array.

    You are given an integer array `nums` and an integer `k`. In one operation, you can choose an index of `nums` and increment the element at that index by `1`.

    Return *the* ***maximum possible frequency*** *of an element after performing* ***at most*** `k` *operations*.

    ## Examples

    ```
    Input: nums = [1,2,4], k = 5
    Output: 3
    ```
    **Explanation:** Increment the first element three times and the second element two times to make nums = [4,4,4].
    4 has a frequency of 3.

    ```
    Input: nums = [1,4,8,13], k = 5
    Output: 2
    ```
    **Explanation:** There are multiple optimal solutions:
    - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
    - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
    - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

    ```
    Input: nums = [3,9,6], k = 2
    Output: 1
    ```

    ## Constraints

    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^5
    - 1 <= k <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_frequency(self, nums: list[int], k: int) -> int:
            raise NotImplementedError('Implement max_frequency')

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
