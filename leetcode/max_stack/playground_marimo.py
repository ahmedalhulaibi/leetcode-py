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
    # 716. Max Stack

    **Hard** · Linked List, Stack, Design, Doubly-Linked List, Ordered Set

    Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

    Implement the `MaxStack` class:

    - `MaxStack()` Initializes the stack object.
    - `void push(int x)` Pushes element x onto the stack.
    - `int pop()` Removes the element on top of the stack and returns it.
    - `int top()` Gets the element on the top of the stack without removing it.
    - `int peekMax()` Retrieves the maximum element in the stack without removing it.
    - `int popMax()` Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

    You must come up with a solution that supports `O(1)` for each `top` call and `O(logn)` for each other call.

    ## Examples

    ```
    Input
    ['MaxStack', 'push', 'push', 'push', 'top', 'pop_max', 'top', 'peek_max', 'pop', 'top']
    [[], [5], [1], [5], [], [], [], [], [], []]
    Output
    [null, null, null, null, 5, 5, 1, 5, 1, 5]
    ```

    ## Constraints

    - -10^7 <= x <= 10^7
    - At most 10^5 calls will be made to push, pop, top, peek_max, and pop_max.
    - There will be at least one element in the stack when pop, top, peek_max, or pop_max is called.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class MaxStack:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def push(self, x: int) -> None:
            raise NotImplementedError('Implement push')

        def pop(self) -> int:
            raise NotImplementedError('Implement pop')

        def top(self) -> int:
            raise NotImplementedError('Implement top')

        def peek_max(self) -> int:
            raise NotImplementedError('Implement peek_max')

        def pop_max(self) -> int:
            raise NotImplementedError('Implement pop_max')

    practice_exports = {'MaxStack': MaxStack}
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
