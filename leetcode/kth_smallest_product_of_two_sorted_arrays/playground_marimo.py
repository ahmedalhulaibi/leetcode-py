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
    # 2040. Kth Smallest Product of Two Sorted Arrays

    **Hard** · Array, Binary Search

    Given two **sorted 0-indexed** integer arrays `nums1` and `nums2` as well as an integer `k`, return the `kth` (**1-based**) smallest product of `nums1[i] * nums2[j]` where `0 <= i < nums1.length` and `0 <= j < nums2.length`.

    ## Examples

    ```
    Input: nums1 = [2,5], nums2 = [3,4], k = 2
    Output: 8
    Explanation: The 2 smallest products are:
    - nums1[0] * nums2[0] = 2 * 3 = 6
    - nums1[0] * nums2[1] = 2 * 4 = 8
    The 2nd smallest product is 8.
    ```

    ```
    Input: nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
    Output: 0
    Explanation: The 6 smallest products are:
    - nums1[0] * nums2[1] = (-4) * 4 = -16
    - nums1[0] * nums2[0] = (-4) * 2 = -8
    - nums1[1] * nums2[1] = (-2) * 4 = -8
    - nums1[1] * nums2[0] = (-2) * 2 = -4
    - nums1[2] * nums2[0] = 0 * 2 = 0
    - nums1[2] * nums2[1] = 0 * 4 = 0
    The 6th smallest product is 0.
    ```

    ```
    Input: nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
    Output: -6
    Explanation: The 3 smallest products are:
    - nums1[0] * nums2[4] = (-2) * 5 = -10
    - nums1[0] * nums2[3] = (-2) * 4 = -8
    - nums1[4] * nums2[0] = 2 * (-3) = -6
    The 3rd smallest product is -6.
    ```

    ## Constraints

    - 1 <= nums1.length, nums2.length <= 5 * 10^4
    - -10^5 <= nums1[i], nums2[j] <= 10^5
    - 1 <= k <= nums1.length * nums2.length
    - nums1 and nums2 are sorted.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def kth_smallest_product(self, nums1: list[int], nums2: list[int], k: int) -> int:
            raise NotImplementedError('Implement kth_smallest_product')

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
