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
    # 232. Implement Queue using Stacks

    **Easy** · Stack, Design, Queue

    Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

    Implement the `MyQueue` class:

    - `void push(int x)` Pushes element x to the back of the queue.
    - `int pop()` Removes the element from the front of the queue and returns it.
    - `int peek()` Returns the element at the front of the queue.
    - `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

    ## Examples

    ```
    Input
    ["MyQueue", "push", "push", "peek", "pop", "empty"]
    [[], [1], [2], [], [], []]
    Output
    [null, null, null, 1, 1, false]
    ```
    **Explanation:**
    ```
    MyQueue myQueue = new MyQueue();
    myQueue.push(1); // queue is: [1]
    myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
    myQueue.peek(); // return 1
    myQueue.pop(); // return 1, queue is [2]
    myQueue.empty(); // return false
    ```

    ## Constraints

    - 1 <= x <= 9
    - At most 100 calls will be made to push, pop, peek, and empty.
    - All the calls to pop and peek are valid.

    **Notes:**
    - You must use **only** standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
    - Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

    **Follow-up:** Can you implement the queue such that each operation is amortized `O(1)` time complexity? In other words, performing `n` operations will take overall `O(n)` time even if one of those operations may take longer.

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class MyQueue:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def push(self, x: int) -> None:
            raise NotImplementedError('Implement push')

        def pop(self) -> int:
            raise NotImplementedError('Implement pop')

        def peek(self) -> int:
            raise NotImplementedError('Implement peek')

        def empty(self) -> bool:
            raise NotImplementedError('Implement empty')

    practice_exports = {'MyQueue': MyQueue}
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
