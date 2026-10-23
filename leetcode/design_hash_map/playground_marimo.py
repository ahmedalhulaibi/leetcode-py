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
    # 706. Design HashMap

    **Easy** · Array, Hash Table, Linked List, Design, Hash Function

    Design a HashMap without using any built-in hash table libraries.

    Implement the `MyHashMap` class:

    - `MyHashMap()` initializes the object with an empty map.
    - `void put(int key, int value)` inserts a `(key, value)` pair into the HashMap. If the `key` already exists in the map, update the corresponding `value`.
    - `int get(int key)` returns the `value` to which the specified `key` is mapped, or `-1` if this map contains no mapping for the `key`.
    - `void remove(key)` removes the `key` and its corresponding `value` if the map contains the mapping for the `key`.

    ## Examples

    ```
    Input
    ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
    [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
    Output
    [null, null, null, 1, -1, null, 1, null, -1]

    Explanation
    MyHashMap myHashMap = new MyHashMap();
    myHashMap.put(1, 1); // The map is now [[1,1]]
    myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
    myHashMap.get(1);    // return 1
    myHashMap.get(3);    // return -1 (not found)
    myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (update)
    myHashMap.get(2);    // return 1
    myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
    myHashMap.get(2);    // return -1 (not found)
    ```

    ## Constraints

    - 0 <= key, value <= 10^6
    - At most 10^4 calls will be made to `put`, `get`, and `remove`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class MyHashMap:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def put(self, key: int, value: int) -> None:
            raise NotImplementedError('Implement put')

        def get(self, key: int) -> int:
            raise NotImplementedError('Implement get')

        def remove(self, key: int) -> None:
            raise NotImplementedError('Implement remove')

    practice_exports = {'MyHashMap': MyHashMap}
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
