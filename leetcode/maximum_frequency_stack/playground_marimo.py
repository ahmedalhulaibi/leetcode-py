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
    # 895. Maximum Frequency Stack

    **Hard** · Hash Table, Stack, Design, Ordered Set

    Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

    Implement the `FreqStack` class:

    - `FreqStack()` constructs the empty frequency stack.
    - `void push(int val)` pushes an integer `val` onto the top of the stack.
    - `int pop()` removes and returns the most frequent element in the stack.
      - If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

    ## Examples

    ```
    Input
    ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
    [[], [5], [7], [5], [7], [4], [5], [], [], [], []]

    Output
    [null, null, null, null, null, null, null, 5, 7, 5, 4]
    ```
    **Explanation:**
    ```
    FreqStack freqStack = new FreqStack();
    freqStack.push(5); // The stack is [5]
    freqStack.push(7); // The stack is [5,7]
    freqStack.push(5); // The stack is [5,7,5]
    freqStack.push(7); // The stack is [5,7,5,7]
    freqStack.push(4); // The stack is [5,7,5,7,4]
    freqStack.push(5); // The stack is [5,7,5,7,4,5]
    freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
    freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
    freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
    freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
    ```

    ## Constraints

    - `0 <= val <= 10^9`
    - At most `2 * 10^4` calls will be made to `push` and `pop`.
    - It is guaranteed that there will be at least one element in the stack before calling `pop`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class FreqStack:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def push(self, val: int) -> None:
            raise NotImplementedError('Implement push')

        def pop(self) -> int:
            raise NotImplementedError('Implement pop')

    practice_exports = {'FreqStack': FreqStack}
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
