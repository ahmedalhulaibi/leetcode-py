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
    # 384. Shuffle an Array

    **Medium** · Array, Math, Design, Randomized

    Given an integer array `nums`, design an algorithm to randomly shuffle the array. All permutations of the array should be **equally likely** as a result of the shuffling.

    Implement the `Solution` class:

    - `Solution(int[] nums)` Initializes the object with the integer array `nums`.
    - `int[] reset()` Resets the array to its original configuration and returns it.
    - `int[] shuffle()` Returns a random shuffling of the array.

    ## Examples

    ```
    Input
    ["Solution", "shuffle", "reset", "shuffle"]
    [[[1, 2, 3]], [], [], []]
    Output
    [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

    Explanation
    Solution solution = new Solution([1, 2, 3]);
    solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                           // Any permutation of [1,2,3] must be equally likely to be returned. Example: return [3, 1, 2]
    solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
    solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]
    ```

    ## Constraints

    - `1 <= nums.length <= 50`
    - `-10^6 <= nums[i] <= 10^6`
    - All the elements of `nums` are **unique**.
    - At most `10^4` calls in total will be made to `reset` and `shuffle`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    import random

    class Solution:

        def __init__(self, nums: list[int]) -> None:
            raise NotImplementedError('Implement __init__')

        def reset(self) -> list[int]:
            raise NotImplementedError('Implement reset')

        def shuffle(self) -> list[int]:
            raise NotImplementedError('Implement shuffle')

    practice_exports = {'random': random, 'Solution': Solution}
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
