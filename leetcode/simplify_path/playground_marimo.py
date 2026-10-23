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
    # 71. Simplify Path

    **Medium** · String, Stack

    You are given an *absolute* path for a Unix-style file system, which always begins with a slash `/`. Your task is to transform this absolute path into its **simplified canonical path**.

    The *rules* of a Unix-style file system are as follows:

    - A single period `'.'` represents the current directory.
    - A double period `'..'` represents the previous/parent directory.
    - Multiple consecutive slashes such as `'//'` and `'///'` are treated as a single slash `'/'`.
    - Any sequence of periods that does **not match** the rules above should be treated as a **valid directory or file name**. For example, `'...'` and `'....'` are valid directory or file names.

    The simplified canonical path should follow these *rules*:

    - The path must start with a single slash `'/'`.
    - Directories within the path must be separated by exactly one slash `'/'`.
    - The path must not end with a slash `'/'`, unless it is the root directory.
    - The path must not have any single or double periods (`'.'` and `'..'`) used to denote current or parent directories.

    Return the **simplified canonical path**.

    ## Examples

    ```
    Input: path = "/home/"
    Output: "/home"
    ```
    **Explanation:**

    The trailing slash should be removed.

    ```
    Input: path = "/home//foo/"
    Output: "/home/foo"
    ```
    **Explanation:**

    Multiple consecutive slashes are replaced by a single one.

    ```
    Input: path = "/home/user/Documents/../Pictures"
    Output: "/home/user/Pictures"
    ```
    **Explanation:**

    A double period `".."` refers to the directory up a level (the parent directory).

    ```
    Input: path = "/../"
    Output: "/"
    ```
    **Explanation:**

    Going one level up from the root directory is not possible.

    ```
    Input: path = "/.../a/../b/c/../d/./"
    Output: "/.../b/d"
    ```
    **Explanation:**

    `"..."` is a valid name for a directory in this problem.

    ## Constraints

    - 1 <= path.length <= 3000
    - `path` consists of English letters, digits, period `'.'`, slash `'/'` or `'_'`.
    - `path` is a valid absolute Unix path.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def simplify_path(self, path: str) -> str:
            raise NotImplementedError('Implement simplify_path')

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
