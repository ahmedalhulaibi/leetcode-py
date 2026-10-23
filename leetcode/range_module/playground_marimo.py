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
    # 715. Range Module

    **Hard** · Design, Segment Tree, Ordered Set

    A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

    A half-open interval `[left, right)` denotes all the real numbers `x` where `left <= x < right`.

    Implement the `RangeModule` class:

    - `RangeModule()` Initializes the object of the data structure.
    - `void addRange(int left, int right)` Adds the half-open interval `[left, right)`, tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval `[left, right)` that are not already tracked.
    - `boolean queryRange(int left, int right)` Returns `true` if every real number in the interval `[left, right)` is currently being tracked, and `false` otherwise.
    - `void removeRange(int left, int right)` Stops tracking every real number currently being tracked in the half-open interval `[left, right)`.

    ## Examples

    ```
    Input
    ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
    [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
    Output
    [null, null, null, true, false, true]

    Explanation
    RangeModule rangeModule = new RangeModule();
    rangeModule.addRange(10, 20);
    rangeModule.removeRange(14, 16);
    rangeModule.queryRange(10, 14); // return True, (Every number in [10, 14) is being tracked)
    rangeModule.queryRange(13, 15); // return False, (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
    rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
    ```

    ## Constraints

    - `1 <= left < right <= 10^9`
    - At most `10^4` calls will be made to `addRange`, `queryRange`, and `removeRange`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class RangeModule:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def add_range(self, left: int, right: int) -> None:
            raise NotImplementedError('Implement add_range')

        def query_range(self, left: int, right: int) -> bool:
            raise NotImplementedError('Implement query_range')

        def remove_range(self, left: int, right: int) -> None:
            raise NotImplementedError('Implement remove_range')

    practice_exports = {'RangeModule': RangeModule}
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
