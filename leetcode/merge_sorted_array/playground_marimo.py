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
    # 88. Merge Sorted Array

    **Easy** · Array, Two Pointers, Sorting

    You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

    **Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

    The final sorted array should not be returned by the function, but instead be *stored inside the array* `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

    ## Examples

    ```
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    ```
    **Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [<u>1</u>,<u>2</u>,2,<u>3</u>,5,6], with the underlined elements coming from nums1.

    ```
    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    ```
    **Explanation:** The arrays we are merging are [1] and [].
    The result of the merge is [1].

    ```
    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    ```
    **Explanation:** The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

    ## Constraints

    - nums1.length == m + n
    - nums2.length == n
    - 0 <= m, n <= 200
    - 1 <= m + n <= 200
    - -10^9 <= nums1[i], nums2[j] <= 10^9

    **Follow up:** Can you come up with an algorithm that runs in `O(m + n)` time?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
            raise NotImplementedError('Implement merge')

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
