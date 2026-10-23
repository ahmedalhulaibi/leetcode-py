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
    # 641. Design Circular Deque

    **Medium** · Array, Linked List, Design, Queue

    Design your implementation of the circular double-ended queue (deque).

    Implement the `MyCircularDeque` class:

    - `MyCircularDeque(int k)` Initializes the deque with a maximum size of `k`.
    - `boolean insertFront()` Adds an item at the front of Deque. Returns `true` if the operation is successful, or `false` otherwise.
    - `boolean insertLast()` Adds an item at the rear of Deque. Returns `true` if the operation is successful, or `false` otherwise.
    - `boolean deleteFront()` Deletes an item from the front of Deque. Returns `true` if the operation is successful, or `false` otherwise.
    - `boolean deleteLast()` Deletes an item from the rear of Deque. Returns `true` if the operation is successful, or `false` otherwise.
    - `int getFront()` Returns the front item from the Deque. Returns `-1` if the deque is empty.
    - `int getRear()` Returns the last item from Deque. Returns `-1` if the deque is empty.
    - `boolean isEmpty()` Returns `true` if the deque is empty, or `false` otherwise.
    - `boolean isFull()` Returns `true` if the deque is full, or `false` otherwise.

    ## Examples

    ```
    Input
    ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
    [[3], [1], [2], [3], [4], [], [], [], [4], []]
    Output
    [null, true, true, true, false, 2, true, true, true, 4]

    Explanation
    MyCircularDeque myCircularDeque = new MyCircularDeque(3);
    myCircularDeque.insertLast(1);  // return True
    myCircularDeque.insertLast(2);  // return True
    myCircularDeque.insertFront(3); // return True
    myCircularDeque.insertFront(4); // return False, the queue is full.
    myCircularDeque.getRear();      // return 2
    myCircularDeque.isFull();       // return True
    myCircularDeque.deleteLast();   // return True
    myCircularDeque.insertFront(4); // return True
    myCircularDeque.getFront();     // return 4
    ```

    ## Constraints

    - `1 <= k <= 1000`
    - `0 <= value <= 1000`
    - At most `2000` calls will be made to `insertFront`, `insertLast`, `deleteFront`, `deleteLast`, `getFront`, `getRear`, `isEmpty`, `isFull`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class MyCircularDeque:

        def __init__(self, k: int) -> None:
            raise NotImplementedError('Implement __init__')

        def insert_front(self, value: int) -> bool:
            raise NotImplementedError('Implement insert_front')

        def insert_last(self, value: int) -> bool:
            raise NotImplementedError('Implement insert_last')

        def delete_front(self) -> bool:
            raise NotImplementedError('Implement delete_front')

        def delete_last(self) -> bool:
            raise NotImplementedError('Implement delete_last')

        def get_front(self) -> int:
            raise NotImplementedError('Implement get_front')

        def get_rear(self) -> int:
            raise NotImplementedError('Implement get_rear')

        def is_empty(self) -> bool:
            raise NotImplementedError('Implement is_empty')

        def is_full(self) -> bool:
            raise NotImplementedError('Implement is_full')

    practice_exports = {'MyCircularDeque': MyCircularDeque}
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
