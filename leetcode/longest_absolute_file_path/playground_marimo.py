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
    mo.md(r"""
    # 388. Longest Absolute File Path

    **Medium** · String, Stack, Depth-First Search

    Suppose we have a file system that stores both files and directories. An example of one system is represented in the following picture:

    ![File system](https://assets.leetcode.com/uploads/2020/08/28/mdir.jpg)

    Here, we have `dir` as the only directory in the root. `dir` contains two subdirectories, `subdir1` and `subdir2`. `subdir1` contains a file `file1.ext` and subdirectory `subsubdir1`. `subdir2` contains a subdirectory `subsubdir2`, which contains a file `file2.ext`.

    In text form, it looks like this (where each indented line is one level deeper):

    ```
    dir
        subdir1
            file1.ext
            subsubdir1
        subdir2
            subsubdir2
                file2.ext
    ```

    If we were to write this representation in code, it will look like this: `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"`. Note that the `'\n'` and `'\t'` are the new-line and tab characters.

    Every file and directory has a unique **absolute path** in the file system, which is the order of directories that must be opened to reach the file/directory itself, all concatenated by `'/'`s. Using the above example, the **absolute path** to `file2.ext` is `"dir/subdir2/subsubdir2/file2.ext"`. Each directory name consists of letters, digits, and/or spaces. Each file name is of the form `name.extension`, where `name` and `extension` consist of letters, digits, and/or spaces.

    Given a string `input` representing the file system in the explained format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return `0`.

    Note that the testcases are generated such that the file system is valid and no file or directory name has length 0.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/08/28/dir1.jpg)

    ```
    Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    Output: 20
    ```

    Explanation: We have only one file, and the absolute path is `"dir/subdir2/file.ext"` of length 20.

    ![Example 2](https://assets.leetcode.com/uploads/2020/08/28/dir2.jpg)

    ```
    Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    Output: 32
    ```

    Explanation: We have two files: `"dir/subdir1/file1.ext"` of length 21 and `"dir/subdir2/subsubdir2/file2.ext"` of length 32. We return 32 since it is the longest absolute path to a file.

    ```
    Input: input = "a"
    Output: 0
    ```

    Explanation: We do not have any files, just a single directory named `"a"`.

    ## Constraints

    - 1 <= input.length <= 10^4
    - `input` may contain lowercase or uppercase English letters, a new line character `'\n'`, a tab character `'\t'`, a dot `'.'`, a space `' '`, and digits.
    - All file and directory names have positive length.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def length_longest_path(self, input_str: str) -> int:
            raise NotImplementedError('Implement length_longest_path')

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
