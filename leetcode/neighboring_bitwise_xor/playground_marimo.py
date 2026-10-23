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
    # 2683. Neighboring Bitwise XOR

    **Medium** · Array, Bit Manipulation

    A **0-indexed** array `derived` with length `n` is derived by computing the **bitwise XOR** (`⊕`) of adjacent values in a **binary array** `original` of length `n`.

    Specifically, for each index `i` in the range `[0, n - 1]`:

    - If `i = n - 1`, then `derived[i] = original[i] ⊕ original[0]`.
    - Otherwise, `derived[i] = original[i] ⊕ original[i + 1]`.

    Given an array `derived`, your task is to determine whether there exists a **valid binary array** `original` that could have formed `derived`.

    Return `true` if such an array exists or `false` otherwise.

    - A binary array is an array containing only `0`'s and `1`'s

    ## Examples

    ```
    Input: derived = [1,1,0]
    Output: true
    Explanation: A valid original array that gives derived is [0,1,0].
    derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1
    derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1
    derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0
    ```

    ```
    Input: derived = [1,1]
    Output: true
    Explanation: A valid original array that gives derived is [0,1].
    derived[0] = original[0] ⊕ original[1] = 1
    derived[1] = original[1] ⊕ original[0] = 1
    ```

    ```
    Input: derived = [1,0]
    Output: false
    Explanation: There is no valid original array that gives derived.
    ```

    ## Constraints

    - n == derived.length
    - 1 <= n <= 10^5
    - The values in derived are either 0's or 1's



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def does_valid_array_exist(self, derived: list[int]) -> bool:
            raise NotImplementedError('Implement does_valid_array_exist')

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
