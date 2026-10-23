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
    # 622. Design Circular Queue

    **Medium** · Array, Linked List, Design, Queue

    Design your implementation of the circular queue. The circular queue is a linear data structure that operates on the FIFO (First In First Out) principle, with the last position connected back to the first to form a circle (a "Ring Buffer").

    Implement the `MyCircularQueue` class:

    - `MyCircularQueue(k)` Initializes the object with the queue size `k`.
    - `int Front()` Gets the front item; returns `-1` if empty.
    - `int Rear()` Gets the last item; returns `-1` if empty.
    - `boolean enQueue(int value)` Inserts an element. Returns `true` if successful.
    - `boolean deQueue()` Deletes an element from the queue. Returns `true` if successful.
    - `boolean isEmpty()` Checks whether the queue is empty.
    - `boolean isFull()` Checks whether the queue is full.

    You must solve the problem without using the built-in queue data structure.

    ## Examples

    ```
    Input
    ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
    [[3], [1], [2], [3], [4], [], [], [], [4], []]
    Output
    [null, true, true, true, false, 3, true, true, true, 4]

    Explanation
    myCircularQueue = MyCircularQueue(3);
    myCircularQueue.enQueue(1);  // True
    myCircularQueue.enQueue(2);  // True
    myCircularQueue.enQueue(3);  // True
    myCircularQueue.enQueue(4);  // False, queue is full
    myCircularQueue.Rear();      // 3
    myCircularQueue.isFull();    // True
    myCircularQueue.deQueue();   // True
    myCircularQueue.enQueue(4);  // True
    myCircularQueue.Rear();      // 4
    ```

    ## Constraints

    - 1 <= k <= 1000
    - 0 <= value <= 1000
    - At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class MyCircularQueue:

        def __init__(self, k: int) -> None:
            raise NotImplementedError('Implement __init__')

        def en_queue(self, value: int) -> bool:
            raise NotImplementedError('Implement en_queue')

        def de_queue(self) -> bool:
            raise NotImplementedError('Implement de_queue')

        def front(self) -> int:
            raise NotImplementedError('Implement front')

        def rear(self) -> int:
            raise NotImplementedError('Implement rear')

        def is_empty(self) -> bool:
            raise NotImplementedError('Implement is_empty')

        def is_full(self) -> bool:
            raise NotImplementedError('Implement is_full')

    practice_exports = {'MyCircularQueue': MyCircularQueue}
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
