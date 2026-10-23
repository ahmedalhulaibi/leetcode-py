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
    # 251. Flatten 2D Vector

    **Medium** · Design, Array, Two Pointers, Iterator

    Design an iterator to flatten a 2D vector. It should support the `next` and `hasNext` operations.

    Implement the `Vector2D` class:

    - `Vector2D(int[][] vec)` initializes the object with the 2D vector `vec`.
    - `next()` returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to `next` are valid.
    - `hasNext()` returns `true` if there are still some elements in the vector, and `false` otherwise.

    ## Examples

    ```
    Input
    ["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
    [[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
    Output
    [null, 1, 2, 3, true, true, 4, false]

    Explanation
    Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
    vector2D.next();    // return 1
    vector2D.next();    // return 2
    vector2D.next();    // return 3
    vector2D.hasNext(); // return True
    vector2D.hasNext(); // return True
    vector2D.next();    // return 4
    vector2D.hasNext(); // return False
    ```

    ## Constraints

    - `0 <= vec.length <= 200`
    - `0 <= vec[i].length <= 500`
    - `-500 <= vec[i][j] <= 500`
    - At most `10^5` calls will be made to `next` and `hasNext`.

    **Follow up:** As an added challenge, try to code it using only iterators in C++ or iterators in Java.

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Vector2D:

        def __init__(self, vec: list[list[int]]) -> None:
            raise NotImplementedError('Implement __init__')

        def next(self) -> int:
            raise NotImplementedError('Implement next')

        def has_next(self) -> bool:
            raise NotImplementedError('Implement has_next')

    practice_exports = {'Vector2D': Vector2D}
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
