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
    # 677. Map Sum Pairs

    **Medium** · Hash Table, String, Design, Trie

    Design a map that allows you to do the following:

    - Maps a string key to a given value.
    - Returns the sum of the values that have a key with a prefix equal to a given string.

    Implement the `MapSum` class:

    - `MapSum()` Initializes the `MapSum` object.
    - `void insert(String key, int val)` Inserts the `key-val` pair into the map. If the `key` already existed, the original `key-value` pair will be overridden to the new one.
    - `int sum(string prefix)` Returns the sum of all the pairs' value whose `key` starts with the `prefix`.

    ## Examples

    ```
    Input
    ["MapSum", "insert", "sum", "insert", "sum"]
    [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
    Output
    [null, null, 3, null, 5]
    ```

    **Explanation**
    ```
    MapSum mapSum = new MapSum();
    mapSum.insert("apple", 3);
    mapSum.sum("ap");           // return 3 (apple = 3)
    mapSum.insert("app", 2);
    mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
    ```

    ## Constraints

    - `1 <= key.length, prefix.length <= 50`
    - `key` and `prefix` consist of only lowercase English letters.
    - `1 <= val <= 1000`
    - At most `50` calls will be made to `insert` and `sum`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class MapSum:

        def __init__(self) -> 'None':
            raise NotImplementedError('Implement __init__')

        def insert(self, key: 'str', val: 'int') -> 'None':
            raise NotImplementedError('Implement insert')

        def sum(self, prefix: 'str') -> 'int':
            raise NotImplementedError('Implement sum')

    practice_exports = {'MapSum': MapSum}
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
