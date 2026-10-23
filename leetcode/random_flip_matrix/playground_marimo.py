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
    # 519. Random Flip Matrix

    **Medium** · Hash Table, Math, Reservoir Sampling, Randomized

    There is an `m x n` binary grid `matrix` with all the values set `0` initially. Design an algorithm to randomly pick an index `(i, j)` where `matrix[i][j] == 0` and flips it to `1`. All the indices `(i, j)` where `matrix[i][j] == 0` should be equally likely to be returned.

    Optimize your algorithm to minimize the number of calls made to the **built-in** random function of your language and optimize the time and space complexity.

    Implement the `Solution` class:

    - `Solution(int m, int n)` Initializes the object with the size of the binary matrix `m` and `n`.
    - `int[] flip()` Returns a random index `[i, j]` of the matrix where `matrix[i][j] == 0` and flips it to `1`.
    - `void reset()` Resets all the values of the matrix to be `0`.

    ## Examples

    ```
    Input
    ["Solution", "flip", "flip", "flip", "reset", "flip"]
    [[3, 1], [], [], [], [], []]
    Output
    [null, [1, 0], [2, 0], [0, 0], null, [2, 0]]

    Explanation
    Solution solution = new Solution(3, 1);
    solution.flip();  // return [1, 0], [0,0], [1,0], and [2,0] should be equally likely to be returned.
    solution.flip();  // return [2, 0], Since [1,0] was returned, [2,0] and [0,0]
    solution.flip();  // return [0, 0], Based on the previously returned indices, only [0,0] can be returned.
    solution.reset(); // All the values are reset to 0 and can be returned.
    solution.flip();  // return [2, 0], [0,0], [1,0], and [2,0] should be equally likely to be returned.
    ```

    ## Constraints

    - `1 <= m, n <= 10^4`
    - There will be at least one free cell for each call to `flip`.
    - At most `1000` calls will be made to `flip` and `reset`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    import random

    class Solution:

        def __init__(self, m: int, n: int) -> None:
            raise NotImplementedError('Implement __init__')

        def flip(self) -> list[int]:
            raise NotImplementedError('Implement flip')

        def reset(self) -> None:
            raise NotImplementedError('Implement reset')

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
