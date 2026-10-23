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
    # 284. Peeking Iterator

    **Medium** · Array, Design, Iterator

    Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.

    Implement the PeekingIterator class:

    - `PeekingIterator(Iterator<int> nums)` Initializes the object with the given integer iterator `iterator`.
    - `int next()` Returns the next element in the array and moves the pointer to the next element.
    - `boolean hasNext()` Returns `true` if there are still elements in the array.
    - `int peek()` Returns the next element in the array **without** moving the pointer.

    **Note:** Each language may have a different implementation of the constructor and Iterator, but they all support the `int next()` and `boolean hasNext()` functions.

    ## Examples

    ```
    Input
    ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
    [[[1, 2, 3]], [], [], [], [], []]
    Output
    [null, 1, 2, 2, 3, false]

    Explanation
    PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
    peekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].
    peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
    peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3]
    peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
    peekingIterator.hasNext(); // return False
    ```

    ## Constraints

    - `1 <= nums.length <= 1000`
    - `1 <= nums[i] <= 1000`
    - All the calls to `next` and `peek` are valid.
    - At most `1000` calls will be made to `next`, `hasNext`, and `peek`.

    **Follow up:** How would you extend your design to be generic and work with all types, not just integer?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Iterator:

        def __init__(self, nums: list[int]) -> None:
            self._nums: list[int] = list(nums)
            self._index: int = 0

        def next(self) -> int:
            value = self._nums[self._index]
            self._index += 1
            return value

        def has_next(self) -> bool:
            return self._index < len(self._nums)

    class PeekingIterator(Iterator):

        def __init__(self, iterator: Iterator) -> None:
            raise NotImplementedError('Implement __init__')

        def peek(self) -> int:
            raise NotImplementedError('Implement peek')

        def next(self) -> int:
            raise NotImplementedError('Implement next')

        def has_next(self) -> bool:
            raise NotImplementedError('Implement has_next')

    practice_exports = {'Iterator': Iterator, 'PeekingIterator': PeekingIterator}
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
