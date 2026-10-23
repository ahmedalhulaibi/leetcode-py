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
    # 398. Random Pick Index

    **Medium** · Hash Table, Math, Reservoir Sampling, Randomized

    Given an integer array `nums` with possible **duplicates**, randomly output the index of a given `target` number. You can assume that the given target number must exist in the array.

    Implement the `Solution` class:

    - `Solution(int[] nums)` Initializes the object with the array `nums`.
    - `int pick(int target)` Picks a random index `i` from `nums` where `nums[i] == target`. If there are multiple valid `i`'s, then each index should have an equal probability of returning.

    ## Examples

    ```
    Input
    ["Solution", "pick", "pick", "pick"]
    [[[1, 2, 3, 3, 3]], [3], [1], [3]]
    Output
    [null, 4, 0, 2]

    Explanation
    Solution solution = new Solution([1, 2, 3, 3, 3]);
    solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
    solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
    solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
    ```

    ## Constraints

    - `1 <= nums.length <= 2 * 10^4`
    - `-2^31 <= nums[i] <= 2^31 - 1`
    - `target` is an integer from `nums`.
    - At most `10^4` calls will be made to `pick`.

    **Follow up:** What is the time and space complexity of your solution? Could you do it with `O(1)` extra space?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def __init__(self, nums: list[int]) -> None:
            raise NotImplementedError('Implement __init__')

        def pick(self, target: int) -> int:
            raise NotImplementedError('Implement pick')

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
