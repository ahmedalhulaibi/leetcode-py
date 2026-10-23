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
    # 341. Flatten Nested List Iterator

    **Medium** · Stack, Tree, Depth-First Search, Design, Queue, Iterator

    You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

    Implement the `NestedIterator` class:

    - `NestedIterator(List[NestedInteger] nestedList)` Initializes the iterator with the nested list `nestedList`.
    - `int next()` Returns the next integer in the nested list.
    - `boolean hasNext()` Returns `true` if there are still some integers in the nested list and `false` otherwise.

    Your code will be tested with the following pseudocode:

    ```
    initialize iterator with nestedList
    res = []
    while iterator.hasNext()
        append iterator.next() to the end of res
    return res
    ```

    If `res` matches the expected flattened list, then your code will be judged as correct.

    ## Examples

    ```
    Input: nestedList = [[1,1],2,[1,1]]
    Output: [1,1,2,1,1]
    Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
    ```

    ```
    Input: nestedList = [1,[4,[6]]]
    Output: [1,4,6]
    Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
    ```

    ## Constraints

    - 1 <= nestedList.length <= 500
    - The values of the integers in the nested list is in the range [-10<sup>6</sup>, 10<sup>6</sup>].



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from typing import Any

    class NestedIterator:

        def __init__(self, nested_list: list[Any]) -> None:
            raise NotImplementedError('Implement __init__')

        def next(self) -> int:
            raise NotImplementedError('Implement next')

        def has_next(self) -> bool:
            raise NotImplementedError('Implement has_next')

    practice_exports = {'Any': Any, 'NestedIterator': NestedIterator}
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
