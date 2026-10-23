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
    # 1538. Guess the Majority in a Hidden Array

    **Medium** · Array, Math, Interactive

    We have an integer array `nums`, where all the integers in `nums` are **0** or **1**. You will not be given direct access to the array, instead, you will have an **API** `ArrayReader` which has the following functions:

    - `int query(int a, int b, int c, int d)`: where `0 <= a < b < c < d < ArrayReader.length()`. The function returns the distribution of the value of the 4 elements:
      - **4**: if the values of the 4 elements are the same (0 or 1).
      - **2**: if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
      - **0**: if two elements have a value equal to 0 and two elements have a value equal to 1.
    - `int length()`: Returns the size of the array.

    You are allowed to call `query()` **2 * n times** at most where n is equal to `ArrayReader.length()`.

    Return **any** index of the most frequent value in `nums`, in case of tie, return -1.

    ## Examples

    ```
    Input: nums = [0,0,1,0,1,1,1,1]
    Output: 5
    Explanation: The following calls to the API
    reader.length() // returns 8 because there are 8 elements in the hidden array.
    reader.query(0,1,2,3) // returns 2 this is a query that compares the elements nums[0], nums[1], nums[2], nums[3]
    // Three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
    reader.query(4,5,6,7) // returns 4 because nums[4], nums[5], nums[6], nums[7] have the same value.
    We can infer that the most frequent value is found in the last 4 elements.
    Index 2, 4, 6, 7 is also a correct answer.
    ```

    ```
    Input: nums = [0,0,1,1,0]
    Output: 0
    ```

    ```
    Input: nums = [1,0,1,0,1,0,1,0]
    Output: -1
    ```

    ## Constraints

    - `5 <= nums.length <= 10^5`
    - `0 <= nums[i] <= 1`

    **Follow up:** What is the minimum number of calls needed to find the majority element?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class ArrayReader:

        def __init__(self, nums: list[int]) -> None:
            self.nums = nums

        def query(self, a: int, b: int, c: int, d: int) -> int:
            total = sum((self.nums[i] for i in (a, b, c, d)))
            return 4 if total in (0, 4) else 2 if total in (1, 3) else 0

        def length(self) -> int:
            return len(self.nums)

    class Solution:

        def guess_majority(self, reader: ArrayReader) -> int:
            raise NotImplementedError('Implement guess_majority')

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
