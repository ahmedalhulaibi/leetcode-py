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
    # 609. Find Duplicate File in System

    **Medium** · Array, Hash Table, String

    Given a list `paths` of directory info, including the directory path, and all the files with contents in this directory, return *all the duplicate files in the file system in terms of their paths*. You may return the answer in **any order**.

    A group of duplicate files consists of at least two files that have the same content.

    A single directory info string in the input list has the following format:

    ```
    "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
    ```

    It means there are `n` files `(f1.txt, f2.txt ... fn.txt)` with content `(f1_content, f2_content ... fn_content)` respectively in the directory `root/d1/d2/.../dm`. Note that `n >= 1` and `m >= 0`. If `m = 0`, it means the directory is just the root directory.

    The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

    ```
    "directory_path/file_name.txt"
    ```

    ## Examples

    ```
    Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
    Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
    ```

    ```
    Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
    Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
    ```

    ## Constraints

    - `1 <= paths.length <= 2 * 10^4`
    - `1 <= paths[i].length <= 3000`
    - `1 <= sum(paths[i].length) <= 5 * 10^5`
    - `paths[i]` consist of English letters, digits, `'/'`, `'.'`, `'('`, `')'`, and `' '`.
    - You may assume no files or directories share the same name in the same directory.
    - You may assume each given directory info represents a unique directory. A single blank space separates the directory path and file info.

    **Follow up:**

    - Imagine you are given a real file system, how will you search files? DFS or BFS?
    - If the file content is very large (GB level), how will you modify your solution?
    - If you can only read the file by 1kb each time, how will you modify your solution?
    - What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part of it? How to optimize?
    - How to make sure the duplicated files you find are not false positive?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import defaultdict

    class Solution:

        def find_duplicate(self, paths: list[str]) -> list[list[str]]:
            raise NotImplementedError('Implement find_duplicate')

    practice_exports = {'defaultdict': defaultdict, 'Solution': Solution}
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
