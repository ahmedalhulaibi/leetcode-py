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
    # 1598. Crawler Log Folder

    **Easy** · Array, String, Stack

    The Leetcode file system keeps a log each time some user performs a change folder operation.

    The operations are described below:

    - `'../'` : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
    - `'./'` : Remain in the same folder.
    - `'x/'` : Move to the child folder named x (This folder is guaranteed to always exist).

    You are given a list of strings `logs` where `logs[i]` is the operation performed by the user at the ith step.

    The file system starts in the main folder, then the operations in `logs` are performed.

    Return the minimum number of operations needed to go back to the main folder after the change folder operations.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/09/09/sample_11_1957.png)

    ```
    Input: logs = ["d1/","d2/","../","d21/","./"]
    Output: 2
    Explanation: Use this change folder operation "../" 2 times and go back to the main folder.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/09/09/sample_22_1957.png)

    ```
    Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
    Output: 3
    ```

    ```
    Input: logs = ["d1/","../","../","../"]
    Output: 0
    ```

    ## Constraints

    - 1 <= logs.length <= 10^3
    - 2 <= logs[i].length <= 10
    - `logs[i]` contains lowercase English letters, digits, `'.'`, and `'/'`.
    - `logs[i]` follows the format described in the statement.
    - Folder names consist of lowercase English letters and digits.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_operations(self, logs: list[str]) -> int:
            raise NotImplementedError('Implement min_operations')

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
