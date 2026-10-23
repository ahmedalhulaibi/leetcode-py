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
    # 1095. Find in Mountain Array

    **Hard** · Array, Binary Search, Interactive

    (This problem is an **interactive problem**.)

    You may recall that an array `arr` is a **mountain array** if and only if:

    - `arr.length >= 3`
    - There exists some `i` with `0 < i < arr.length - 1` such that:
        - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
        - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

    Given a mountain array `mountainArr`, return **the minimum** `index` such that `mountainArr.get(index) == target`. If such an `index` does not exist, return `-1`.

    **You cannot access the mountain array directly.** You may only access the array using a `MountainArray` interface:

    - `MountainArray.get(k)` returns the element of the array at index `k` (0-indexed).
    - `MountainArray.length()` returns the length of the array.

    Submissions making more than `100` calls to `MountainArray.get` will be judged *Wrong Answer*.

    ## Examples

    ```
    Input: mountainArr = [1,2,3,4,5,3,1], target = 3
    Output: 2
    Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
    ```

    ```
    Input: mountainArr = [0,1,2,4,2,1], target = 3
    Output: -1
    Explanation: 3 does not exist in the array, so we return -1.
    ```

    ## Constraints

    - `3 <= mountainArr.length() <= 10^4`
    - `0 <= target <= 10^9`
    - `0 <= mountainArr.get(index) <= 10^9`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class MountainArray:

        def get(self, index: int) -> int:
            raise NotImplementedError

        def length(self) -> int:
            raise NotImplementedError

    class Solution:

        def find_in_mountain_array(self, target: int, mountain_arr: MountainArray) -> int:
            raise NotImplementedError('Implement find_in_mountain_array')

    practice_exports = {'MountainArray': MountainArray, 'Solution': Solution}
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
