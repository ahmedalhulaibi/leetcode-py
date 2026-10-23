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
    # 307. Range Sum Query - Mutable

    **Medium** · Array, Divide and Conquer, Design, Binary Indexed Tree, Segment Tree, Sqrt Decomposition

    Given an integer array `nums`, handle multiple queries of the following types:

    - **Update** the value of an element in `nums`.
    - Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.

    Implement the `NumArray` class:

    - `NumArray(int[] nums)` Initializes the object with the integer array `nums`.
    - `void update(int index, int val)` **Updates** the value of `nums[index]` to be `val`.
    - `int sumRange(int left, int right)` Returns the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).

    ## Examples

    ```
    Input
    ["NumArray", "sumRange", "update", "sumRange"]
    [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
    Output
    [null, 9, null, 8]

    Explanation
    NumArray numArray = new NumArray([1, 3, 5]);
    numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
    numArray.update(1, 2);   // nums = [1, 2, 5]
    numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
    ```

    ## Constraints

    - `1 <= nums.length <= 3 * 10^4`
    - `-100 <= nums[i] <= 100`
    - `0 <= index < nums.length`
    - `-100 <= val <= 100`
    - `0 <= left <= right < nums.length`
    - At most `3 * 10^4` calls will be made to `update` and `sumRange`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class NumArray:

        def __init__(self, nums: list[int]) -> None:
            raise NotImplementedError('Implement __init__')

        def update(self, index: int, val: int) -> None:
            raise NotImplementedError('Implement update')

        def sum_range(self, left: int, right: int) -> int:
            raise NotImplementedError('Implement sum_range')

    practice_exports = {'NumArray': NumArray}
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
