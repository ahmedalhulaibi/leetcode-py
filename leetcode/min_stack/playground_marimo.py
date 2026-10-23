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
    # 155. Min Stack

    **Medium** · Stack, Design

    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the `MinStack` class:

    - `MinStack()` initializes the stack object.
    - `void push(int val)` pushes the element `val` onto the stack.
    - `void pop()` removes the element on the top of the stack.
    - `int top()` gets the top element of the stack.
    - `int getMin()` retrieves the minimum element in the stack.

    You must implement a solution with `O(1)` time complexity for each function.

    ## Examples

    ```
    Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]
    ```
    **Explanation:**
    ```
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
    ```

    ## Constraints

    - `-2^31 <= val <= 2^31 - 1`
    - Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks.
    - At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class MinStack:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def push(self, val: int) -> None:
            raise NotImplementedError('Implement push')

        def pop(self) -> None:
            raise NotImplementedError('Implement pop')

        def top(self) -> int:
            raise NotImplementedError('Implement top')

        def get_min(self) -> int:
            raise NotImplementedError('Implement get_min')

    practice_exports = {'MinStack': MinStack}
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
