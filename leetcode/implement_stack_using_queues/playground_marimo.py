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
    # 225. Implement Stack using Queues

    **Easy** · Stack, Design, Queue

    Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

    Implement the `MyStack` class:

    - `void push(int x)` Pushes element x to the top of the stack.
    - `int pop()` Removes the element on the top of the stack and returns it.
    - `int top()` Returns the element on the top of the stack.
    - `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

    ## Examples

    ```
    Input
    ["MyStack", "push", "push", "top", "pop", "empty"]
    [[], [1], [2], [], [], []]
    Output
    [null, null, null, 2, 2, false]
    ```
    **Explanation:**
    ```
    MyStack myStack = new MyStack();
    myStack.push(1);
    myStack.push(2);
    myStack.top(); // return 2
    myStack.pop(); // return 2
    myStack.empty(); // return False
    ```

    ## Constraints

    - 1 <= x <= 9
    - At most 100 calls will be made to push, pop, top, and empty.
    - All the calls to pop and top are valid.

    **Notes:**
    - You must use **only** standard operations of a queue, which means that only `push to back`, `peek/pop from front`, `size`, and `is empty` operations are valid.
    - Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

    **Follow-up:** Can you implement the stack using only one queue?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class MyStack:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def push(self, x: int) -> None:
            raise NotImplementedError('Implement push')

        def pop(self) -> int:
            raise NotImplementedError('Implement pop')

        def top(self) -> int:
            raise NotImplementedError('Implement top')

        def empty(self) -> bool:
            raise NotImplementedError('Implement empty')

    practice_exports = {'MyStack': MyStack}
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
