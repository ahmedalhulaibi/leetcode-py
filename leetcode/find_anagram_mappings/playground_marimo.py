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
    # 760. Find Anagram Mappings

    **Easy** · Array, Hash Table

    You are given two integer arrays `nums1` and `nums2` where `nums2` is an anagram of `nums1`. Both arrays may contain duplicates.

    Return an index mapping array `mapping` from `nums1` to `nums2` where `mapping[i] = j` means the `ith` element in `nums1` appears in `nums2` at index `j`. If there are multiple answers, return any of them.

    An array `a` is an anagram of an array `b` means `b` is made by randomizing the order of the elements in `a`.

    ## Examples

    ```
    Input: nums1 = [12,28,46,32,50], nums2 = [50,12,32,46,28]
    Output: [1,4,3,2,0]
    Explanation: As mapping[0] = 1 because the 0th element of nums1 appears at nums2[1], and mapping[1] = 4 because the 1st element of nums1 appears at nums2[4], and so on.
    ```

    ```
    Input: nums1 = [84,46], nums2 = [84,46]
    Output: [0,1]
    ```

    ## Constraints

    - 1 <= nums1.length <= 100
    - nums2.length == nums1.length
    - 0 <= nums1[i], nums2[i] <= 10^5
    - nums2 is an anagram of nums1.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def anagram_mappings(self, nums1: list[int], nums2: list[int]) -> list[int]:
            raise NotImplementedError('Implement anagram_mappings')

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
