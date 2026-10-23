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
    # 753. Cracking the Safe

    **Hard** · String, Depth-First Search, Graph Theory, Eulerian Circuit, Eulerian Path, Eulerian Graph

    There is a safe protected by a password. The password is a sequence of `n` digits where each digit can be in the range `[0, k - 1]`.

    The safe has a peculiar way of checking the password. When you enter in a sequence, it checks the **most recent `n` digits** that were entered each time you type a digit.

    - For example, the correct password is `"345"` and you enter in `"012345"`:
      - After typing `0`, the most recent `3` digits is `"0"`, which is incorrect.
      - After typing `1`, the most recent `3` digits is `"01"`, which is incorrect.
      - After typing `2`, the most recent `3` digits is `"012"`, which is incorrect.
      - After typing `3`, the most recent `3` digits is `"123"`, which is incorrect.
      - After typing `4`, the most recent `3` digits is `"234"`, which is incorrect.
      - After typing `5`, the most recent `3` digits is `"345"`, which is correct and the safe unlocks.

    Return any string of minimum length that will unlock the safe at some point of entering it.

    ## Examples

    ```
    Input: n = 1, k = 2
    Output: "10"
    Explanation: The password is a single digit, so enter each digit. "01" would also unlock the safe.
    ```

    ```
    Input: n = 2, k = 2
    Output: "01100"
    Explanation: For each possible password:
    - "00" is typed in starting from the 4th digit.
    - "01" is typed in starting from the 1st digit.
    - "10" is typed in starting from the 3rd digit.
    - "11" is typed in starting from the 2nd digit.
    Thus "01100" will unlock the safe. "10011", and "11001" would also unlock the safe.
    ```

    ## Constraints

    - `1 <= n <= 4`
    - `1 <= k <= 10`
    - `1 <= k^n <= 4096`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def crack_safe(self, n: int, k: int) -> str:
            raise NotImplementedError('Implement crack_safe')

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
