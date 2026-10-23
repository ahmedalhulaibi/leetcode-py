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
    # 1868. Product of Two Run-Length Encoded Arrays

    **Medium** · Array, Two Pointers

    **Run-length encoding** is a compression algorithm that allows for an integer array `nums` with many segments of **consecutive repeated** numbers to be represented by a (generally smaller) 2D array `encoded`. Each `encoded[i] = [val_i, freq_i]` describes the `i`-th segment of repeated numbers in `nums` where `val_i` is the value that is repeated `freq_i` times.

    - For example, `nums = [1,1,1,2,2,2,2,2]` is represented by the **run-length encoded** array `encoded = [[1,3],[2,5]]`. Another way to read this is "three `1`'s followed by five `2`'s".

    The **product** of two run-length encoded arrays `encoded1` and `encoded2` can be calculated using the following steps:

    1. **Expand** both `encoded1` and `encoded2` into the full arrays `nums1` and `nums2` respectively.
    2. Create a new array `prodNums` of length `nums1.length` and set `prodNums[i] = nums1[i] * nums2[i]`.
    3. **Compress** `prodNums` into a run-length encoded array and return it.

    You are given two **run-length encoded** arrays `encoded1` and `encoded2` representing full arrays `nums1` and `nums2` respectively. Both `nums1` and `nums2` have the **same length**. Each `encoded1[i] = [val_i, freq_i]` describes the `i`-th segment of `nums1`, and each `encoded2[j] = [val_j, freq_j]` describes the `j`-th segment of `nums2`.

    Return *the **product** of* `encoded1` *and* `encoded2`.

    **Note:** Compression should be done such that the run-length encoded array has the **minimum** possible length.

    ## Examples

    ```
    Input: encoded1 = [[1,3],[2,3]], encoded2 = [[6,3],[3,3]]
    Output: [[6,6]]
    Explanation: encoded1 expands to [1,1,1,2,2,2] and encoded2 expands to [6,6,6,3,3,3].
    prodNums = [6,6,6,6,6,6], which is compressed into the run-length encoded array [[6,6]].
    ```

    ```
    Input: encoded1 = [[1,3],[2,1],[3,2]], encoded2 = [[2,3],[3,3]]
    Output: [[2,3],[6,1],[9,2]]
    Explanation: encoded1 expands to [1,1,1,2,3,3] and encoded2 expands to [2,2,2,3,3,3].
    prodNums = [2,2,2,6,9,9], which is compressed into the run-length encoded array [[2,3],[6,1],[9,2]].
    ```

    ## Constraints

    - 1 <= encoded1.length, encoded2.length <= 10^5
    - encoded1[i].length == 2
    - encoded2[j].length == 2
    - 1 <= val_i, freq_i <= 10^4 for each encoded1[i]
    - 1 <= val_j, freq_j <= 10^4 for each encoded2[j]
    - The full arrays that encoded1 and encoded2 represent are the same length.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_rle_array(self, encoded1: list[list[int]], encoded2: list[list[int]]) -> list[list[int]]:
            raise NotImplementedError('Implement find_rle_array')

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
