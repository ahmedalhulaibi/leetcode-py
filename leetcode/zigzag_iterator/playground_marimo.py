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
    # 281. Zigzag Iterator

    **Medium** · Design, Queue, Array, Iterator

    Given two vectors of integers `v1` and `v2`, implement an iterator to return their elements alternately.

    Implement the `ZigzagIterator` class:

    - `ZigzagIterator(List<int> v1, List<int> v2)` initializes the object with the two vectors `v1` and `v2`.
    - `boolean hasNext()` returns `true` if the iterator still has elements, and `false` otherwise.
    - `int next()` returns the current element of the iterator and moves the iterator to the next element.

    **Follow up:** What if you are given `k` vectors? How well can your code be extended to such cases?

    ## Examples

    ```
    Input: v1 = [1,2], v2 = [3,4,5,6]
    Output: [1,3,2,4,5,6]
    Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
    ```

    ```
    Input: v1 = [1], v2 = []
    Output: [1]
    ```

    ```
    Input: v1 = [], v2 = [1]
    Output: [1]
    ```

    ## Constraints

    - `0 <= v1.length, v2.length <= 1000`
    - `1 <= v1.length + v2.length <= 2000`
    - `-10^9 <= v1[i], v2[i] <= 10^9`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import deque

    class ZigzagIterator:

        def __init__(self, v1: list[int], v2: list[int]) -> None:
            raise NotImplementedError('Implement __init__')

        def next(self) -> int:
            raise NotImplementedError('Implement next')

        def has_next(self) -> bool:
            raise NotImplementedError('Implement has_next')

    practice_exports = {'deque': deque, 'ZigzagIterator': ZigzagIterator}
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
