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
    # 1533. Find the Index of the Large Integer

    **Medium** · Array, Binary Search, Interactive

    We have an integer array `arr`, where all the integers in `arr` are equal except for one integer which is **larger** than the rest of the integers. You will not be given direct access to the array, instead, you will have an **API** `ArrayReader` which has the following functions:

    - `int compareSub(int l, int r, int x, int y)`: where `0 <= l, r, x, y < ArrayReader.length()`, `l <= r` and `x <= y`. The function compares the sum of sub-array `arr[l..r]` with the sum of the sub-array `arr[x..y]` and returns:
      - **1** if `arr[l]+arr[l+1]+...+arr[r] > arr[x]+arr[x+1]+...+arr[y]`.
      - **0** if `arr[l]+arr[l+1]+...+arr[r] == arr[x]+arr[x+1]+...+arr[y]`.
      - **-1** if `arr[l]+arr[l+1]+...+arr[r] < arr[x]+arr[x+1]+...+arr[y]`.
    - `int length()`: Returns the size of the array.

    You are allowed to call `compareSub()` **20 times** at most. You can assume both functions work in `O(1)` time.

    Return *the index of the array `arr` which has the largest integer*.

    ## Examples

    ```
    Input: arr = [7,7,7,7,10,7,7,7]
    Output: 4
    Explanation: The following calls to the API
    reader.compareSub(0, 0, 1, 1) // returns 0, this is a query comparing the sub-array (0, 0) with the sub array (1, 1), (i.e. compares arr[0] with arr[1]).
    Thus we know that arr[0] and arr[1] doesn't contain the largest element.
    reader.compareSub(2, 2, 3, 3) // returns 0, we can exclude arr[2] and arr[3].
    reader.compareSub(4, 4, 5, 5) // returns 1, thus for sure arr[4] is the largest element in the array.
    Notice that we made only 3 calls, so the answer is valid.
    ```

    ```
    Input: arr = [6,6,12]
    Output: 2
    ```

    ## Constraints

    - `2 <= arr.length <= 5 * 10^5`
    - `1 <= arr[i] <= 100`
    - All elements of `arr` are equal except for one element which is larger than all other elements.

    **Follow up:**

    - What if there are two numbers in `arr` that are bigger than all other numbers?
    - What if there is one number that is bigger than other numbers and one number that is smaller than other numbers?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class ArrayReader:

        def __init__(self, arr: list[int]) -> None:
            self.arr = arr

        def compare_sub(self, lo1: int, hi1: int, lo2: int, hi2: int) -> int:
            left = sum(self.arr[lo1:hi1 + 1])
            right = sum(self.arr[lo2:hi2 + 1])
            return (left > right) - (left < right)

        def length(self) -> int:
            return len(self.arr)

    class Solution:

        def get_index(self, reader: ArrayReader) -> int:
            raise NotImplementedError('Implement get_index')

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
