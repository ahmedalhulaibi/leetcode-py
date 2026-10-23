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
    # 432. All O`one Data Structure

    **Hard** · Hash Table, Linked List, Design, Doubly-Linked List

    Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

    Implement the `AllOne` class:

    - `AllOne()` Initializes the object of the data structure.
    - `inc(String key)` Increments the count of the string `key` by `1`. If `key` does not exist in the data structure, insert it with count `1`.
    - `dec(String key)` Decrements the count of the string `key` by `1`. If the count of `key` is `0` after the decrement, remove it from the data structure. It is guaranteed that `key` exists in the data structure before the decrement.
    - `getMaxKey()` Returns one of the keys with the maximal count. If no element exists, return an empty string `"\"`.
    - `getMinKey()` Returns one of the keys with the minimum count. If no element exists, return an empty string `"\"`.

    Note that each function must run in `O(1)` average time complexity.

    ## Examples

    ```
    Input
    ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
    [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
    Output
    [null, null, null, "hello", "hello", null, "hello", "leet"]

    Explanation
    AllOne allOne = new AllOne();
    allOne.inc("hello");
    allOne.inc("hello");
    allOne.getMaxKey(); // return "hello"
    allOne.getMinKey(); // return "hello"
    allOne.inc("leet");
    allOne.getMaxKey(); // return "hello"
    allOne.getMinKey(); // return "leet"
    ```

    ## Constraints

    - `1 <= key.length <= 10`
    - `key` consists of lowercase English letters.
    - It is guaranteed that for each call to `dec`, `key` exists in the data structure.
    - At most `5 * 10^4` calls will be made to `inc`, `dec`, `getMaxKey`, and `getMinKey`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Bucket:

        def __init__(self, count: 'int') -> 'None':
            self.count = count
            self.keys: 'set[str]' = set()
            self.prev: 'Bucket' = self
            self.next: 'Bucket' = self

        def insert_after(self, node: 'Bucket') -> 'None':
            node.prev = self
            node.next = self.next
            self.next.prev = node
            self.next = node

        def unlink(self) -> 'None':
            self.prev.next = self.next
            self.next.prev = self.prev
            self.prev = self.next = self

    class AllOne:

        def __init__(self) -> 'None':
            raise NotImplementedError('Implement __init__')

        def inc(self, key: 'str') -> 'None':
            raise NotImplementedError('Implement inc')

        def dec(self, key: 'str') -> 'None':
            raise NotImplementedError('Implement dec')

        def get_max_key(self) -> 'str':
            raise NotImplementedError('Implement get_max_key')

        def get_min_key(self) -> 'str':
            raise NotImplementedError('Implement get_min_key')

    practice_exports = {'Bucket': Bucket, 'AllOne': AllOne}
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
