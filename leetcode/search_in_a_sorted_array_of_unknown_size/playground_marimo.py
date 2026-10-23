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
    # 702. Search in a Sorted Array of Unknown Size

    **Medium** · Array, Binary Search, Interactive

    This is an <strong><em>interactive problem</em></strong>.

    You have a sorted array of <strong>unique</strong> elements and an <strong>unknown size</strong>. You do not have an access to the array but you can use the <code>ArrayReader</code> interface to access it. You can call <code>ArrayReader.get(i)</code> that:

    <ul>
    <li>returns the value at the <code>i<sup>th</sup></code> index (<strong>0-indexed</strong>) of the secret array (i.e., <code>secret[i]</code>), or</li>
    <li>returns <code>2<sup>31</sup> - 1</code> if the <code>i</code> is out of the boundary of the array.</li>
    </ul>

    You are also given an integer <code>target</code>.

    Return the index <code>k</code> of the hidden array where <code>secret[k] == target</code> or return <code>-1</code> otherwise.

    You must write an algorithm with <code>O(log n)</code> runtime complexity.

    ## Examples

    ```
    Input: secret = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in secret and its index is 4.
    ```

    ```
    Input: secret = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in secret so return -1.
    ```

    ## Constraints

    - `1 <= secret.length <= 10^4`
    - `-10^4 <= secret[i], target <= 10^4`
    - All the integers of `secret` are <strong>unique</strong>.
    - `secret` is sorted in a strictly increasing order.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class ArrayReader:

        def __init__(self, secret: list[int]) -> None:
            self.secret = secret

        def get(self, index: int) -> int:
            if 0 <= index < len(self.secret):
                return self.secret[index]
            return 2147483647

    class Solution:

        def search(self, reader: ArrayReader, target: int) -> int:
            raise NotImplementedError('Implement search')

    practice_exports = {'ArrayReader': ArrayReader, 'Solution': Solution}
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
