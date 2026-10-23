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
    # 707. Design Linked List

    **Medium** · Linked List, Design

    Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
    A node in a singly linked list should have two attributes: `val` and `next`. `val` is the value of the current node, and `next` is a pointer/reference to the next node.
    If you want to use the doubly linked list, you will need one more attribute `prev` to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

    Implement the `MyLinkedList` class:

    - `MyLinkedList()` Initializes the `MyLinkedList` object.
    - `int get(index)` Get the value of the `indexth` node in the linked list. If the index is invalid, return `-1`.
    - `void addAtHead(int val)` Add a node of value `val` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    - `void addAtTail(int val)` Append a node of value `val` as the last element of the linked list.
    - `void addAtIndex(int index, int val)` Add a node of value `val` before the `indexth` node in the linked list. If `index` equals the length of the linked list, the node will be appended to the end of the linked list. If `index` is greater than the length, the node will not be inserted.
    - `void deleteAtIndex(int index)` Delete the `indexth` node in the linked list, if the index is valid.

    ## Examples

    ```
    Input
    ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    [[], [1], [3], [1, 2], [1], [1], [1]]
    Output
    [null, null, null, null, 2, null, 3]

    Explanation
    MyLinkedList myLinkedList = new MyLinkedList();
    myLinkedList.addAtHead(1);
    myLinkedList.addAtTail(3);
    myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
    myLinkedList.get(1);              // return 2
    myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
    myLinkedList.get(1);              // return 3
    ```

    ## Constraints

    - 0 <= index, val <= 1000
    - Please do not use the built-in LinkedList library.
    - At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class MyLinkedList:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def get(self, index: int) -> int:
            raise NotImplementedError('Implement get')

        def add_at_head(self, val: int) -> None:
            raise NotImplementedError('Implement add_at_head')

        def add_at_tail(self, val: int) -> None:
            raise NotImplementedError('Implement add_at_tail')

        def add_at_index(self, index: int, val: int) -> None:
            raise NotImplementedError('Implement add_at_index')

        def delete_at_index(self, index: int) -> None:
            raise NotImplementedError('Implement delete_at_index')

    practice_exports = {'MyLinkedList': MyLinkedList}
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
