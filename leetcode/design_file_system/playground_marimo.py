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
    # 1166. Design File System

    **Medium** · Design, Trie, Hash Table, String

    You are asked to design a file system that allows you to create new paths and associate them with different values.

    The format of a path is one or more concatenated strings of the form: `/` followed by one or more lowercase English letters. For example, `'/leetcode'` and `'/leetcode/problems'` are valid paths while an empty string `''` and `'/'` are not.

    Implement the `FileSystem` class:

    - `bool createPath(string path, int value)` Creates a new `path` and associates a `value` to it if possible and returns `true`. Returns `false` if the path **already exists** or its parent path **doesn't exist**.
    - `int get(string path)` Returns the value associated with `path` or returns `-1` if the path doesn't exist.

    ## Examples

    ```
    Input:
    ["FileSystem","createPath","get"]
    [[],["/a",1],["/a"]]
    Output:
    [null,true,1]
    Explanation:
    FileSystem fileSystem = new FileSystem();

    fileSystem.createPath("/a", 1); // return true
    fileSystem.get("/a"); // return 1
    ```

    ```
    Input:
    ["FileSystem","createPath","createPath","get","createPath","get"]
    [[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
    Output:
    [null,true,true,2,false,-1]
    Explanation:
    FileSystem fileSystem = new FileSystem();

    fileSystem.createPath("/leet", 1); // return true
    fileSystem.createPath("/leet/code", 2); // return true
    fileSystem.get("/leet/code"); // return 2
    fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
    fileSystem.get("/c"); // return -1 because this path doesn't exist.
    ```

    ## Constraints

    - `2 <= path.length <= 100`
    - `1 <= value <= 10^9`
    - Each `path` is **valid** and consists of lowercase English letters and `'/'`.
    - At most `10^4` calls **in total** will be made to `createPath` and `get`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class FileSystem:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def create_path(self, path: str, value: int) -> bool:
            raise NotImplementedError('Implement create_path')

        def get(self, path: str) -> int:
            raise NotImplementedError('Implement get')

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
