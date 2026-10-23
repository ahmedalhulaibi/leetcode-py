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
    # 1442. Count Triplets That Can Form Two Arrays of Equal XOR

    **Medium** · Array, Hash Table, Math, Bit Manipulation, Prefix Sum

    Given an array of integers `arr`.

    We want to select three indices `i`, `j` and `k` where `(0 <= i < j <= k < arr.length)`.

    Let's define `a` and `b` as follows:

    - `a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]`
    - `b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]`

    Note that `^` denotes the **bitwise-xor** operation.

    Return *the number of triplets* (`i`, `j` and `k`) Where `a == b`.

    ## Examples

    ```
    Input: arr = [2,3,1,6,7]
    Output: 4
    Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
    ```

    ```
    Input: arr = [1,1,1,1,1]
    Output: 10
    ```

    ## Constraints

    - `1 <= arr.length <= 300`
    - `1 <= arr[i] <= 10^8`

    **Follow up:** Can you solve it in `O(n)` time?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_triplets(self, arr: list[int]) -> int:
            raise NotImplementedError('Implement count_triplets')

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
