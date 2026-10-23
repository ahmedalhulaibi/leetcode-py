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
    # 588. Design In-Memory File System

    **Hard** · Design, Trie, Hash Table, String

    Design an in-memory file system to simulate the following functions:

    `ls`: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names **in this directory**. Your output (file and directory names together) should in **lexicographic order**.

    `mkdir`: Given a **directory path** that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

    `addContentToFile`: Given a **file path** and **file content** in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to **append** given content to original content. This function has void return type.

    `readContentFromFile`: Given a **file path**, return its **content** in string format.

    ## Examples

    ![filesystem](https://assets.leetcode.com/uploads/2018/10/12/filesystem.png)

    ```
    Input:
    ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
    [[],["/"],["a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

    Output:
    [null,[],null,null,["a"],"hello"]
    ```

    ## Constraints

    - You can assume all file or directory paths are absolute paths which begin with `/` and do not end with `/` except that the path is just `"/"`.
    - You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
    - You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class FileSystem:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def ls(self, path: str) -> list[str]:
            raise NotImplementedError('Implement ls')

        def mkdir(self, path: str) -> None:
            raise NotImplementedError('Implement mkdir')

        def add_content_to_file(self, file_path: str, content: str) -> None:
            raise NotImplementedError('Implement add_content_to_file')

        def read_content_from_file(self, file_path: str) -> str:
            raise NotImplementedError('Implement read_content_from_file')

    practice_exports = {'FileSystem': FileSystem}
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
