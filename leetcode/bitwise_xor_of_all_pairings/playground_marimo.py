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
    # 2425. Bitwise XOR of All Pairings

    **Medium** · Array, Bit Manipulation, Brainteaser

    You are given two **0-indexed** arrays, `nums1` and `nums2`, consisting of non-negative integers. Let there be another array, `nums3`, which contains the bitwise XOR of **all pairings** of integers between `nums1` and `nums2` (every integer in `nums1` is paired with every integer in `nums2` **exactly once**).

    Return the bitwise XOR of all integers in `nums3`.

    ## Examples

    ```
    Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
    Output: 13
    Explanation:
    A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
    The bitwise XOR of all these numbers is 13, so we return 13.
    ```

    ```
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 0
    Explanation:
    All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^ nums2[1], nums1[1] ^ nums2[0],
    and nums1[1] ^ nums2[1].
    Thus, one possible nums3 array is [2,5,1,6].
    2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.
    ```

    ## Constraints

    - 1 <= nums1.length, nums2.length <= 10^5
    - 0 <= nums1[i], nums2[j] <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def xor_all_nums(self, nums1: list[int], nums2: list[int]) -> int:
            raise NotImplementedError('Implement xor_all_nums')

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
