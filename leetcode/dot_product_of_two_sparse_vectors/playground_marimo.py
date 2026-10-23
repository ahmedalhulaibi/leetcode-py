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
    # 1570. Dot Product of Two Sparse Vectors

    **Medium** · Design, Array, Hash Table, Two Pointers, Linear Algebra

    Given two sparse vectors, compute their dot product.

    Implement class `SparseVector`:

    - `SparseVector(nums)` Initializes the object with the vector `nums`
    - `dotProduct(vec)` Compute the dot product between the instance of *SparseVector* and `vec`

    A **sparse vector** is a vector that has mostly zero values, you should store the sparse vector **efficiently** and compute the dot product between two *SparseVector*.

    ## Examples

    ```
    Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
    Output: 8
    Explanation: v1 = SparseVector(nums1), v2 = SparseVector(nums2)
    v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
    ```

    ```
    Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
    Output: 0
    Explanation: v1 = SparseVector(nums1), v2 = SparseVector(nums2)
    v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
    ```

    ```
    Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
    Output: 6
    ```

    ## Constraints

    - `n == nums1.length == nums2.length`
    - `1 <= n <= 10^5`
    - `0 <= nums1[i], nums2[i] <= 100`

    **Follow up:** What if only one of the vectors is sparse?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class SparseVector:

        def __init__(self, nums: 'list[int]') -> 'None':
            raise NotImplementedError('Implement __init__')

        def dot_product(self, vec: 'SparseVector') -> 'int':
            raise NotImplementedError('Implement dot_product')

    practice_exports = {'SparseVector': SparseVector}
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
