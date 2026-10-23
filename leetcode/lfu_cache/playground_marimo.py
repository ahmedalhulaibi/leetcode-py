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
    # 460. LFU Cache

    **Hard** · Hash Table, Linked List, Design, Doubly-Linked List

    Design and implement a data structure for a Least Frequently Used (LFU) cache.

    Implement the `LFUCache` class:

    - `LFUCache(int capacity)` Initializes the object with the `capacity` of the data structure.
    - `int get(int key)` Gets the value of the `key` if the `key` exists in the cache. Otherwise, returns `-1`.
    - `void put(int key, int value)` Update the value of the `key` if present, or inserts the `key` if not already present. When the cache reaches its `capacity`, it should invalidate and remove the **least frequently used** key before inserting a new item. For this problem, when there is a **tie** (i.e., two or more keys with the same frequency), the **least recently used** `key` would be invalidated.

    A **use counter** is maintained for each key. The key with the smallest use counter is the least frequently used key. When a key is first inserted, its use counter is set to `1` (due to the `put` operation). The use counter is incremented each time `get` or `put` is called on it.

    Both `get` and `put` must run in `O(1)` average time complexity.

    ## Examples

    ```
    Input
    ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    Output
    [null, null, null, 1, null, -1, 3, null, -1, 3, 4]

    Explanation
    lfu = LFUCache(2);
    lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
    lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
    lfu.get(1);      // return 1, cache=[1,2], cnt(2)=1, cnt(1)=2
    lfu.put(3, 3);   // 2 is LFU (cnt=1 smallest), invalidate 2. cache=[3,1]
    lfu.get(2);      // return -1
    lfu.get(3);      // return 3, cnt(3)=2, cnt(1)=2
    lfu.put(4, 4);   // tie cnt 1 and 3, 1 is LRU, invalidate 1. cache=[4,3]
    lfu.get(1);      // return -1
    lfu.get(3);      // return 3, cnt(3)=3, cnt(4)=1
    lfu.get(4);      // return 4, cnt(4)=2, cnt(3)=3
    ```

    ## Constraints

    - 1 <= capacity <= 10^4
    - 0 <= key <= 10^5
    - 0 <= value <= 10^9
    - At most 2 * 10^5 calls will be made to `get` and `put`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import OrderedDict, defaultdict

    class LFUCache:

        def __init__(self, capacity: int) -> None:
            raise NotImplementedError('Implement __init__')

        def get(self, key: int) -> int:
            raise NotImplementedError('Implement get')

        def put(self, key: int, value: int) -> None:
            raise NotImplementedError('Implement put')

    practice_exports = {'OrderedDict': OrderedDict, 'defaultdict': defaultdict, 'LFUCache': LFUCache}
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
