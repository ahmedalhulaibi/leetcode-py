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
    # 352. Data Stream as Disjoint Intervals

    **Hard** · Hash Table, Binary Search, Union-Find, Design, Data Stream, Ordered Set

    Given a data stream input of non-negative integers `a1, a2, ..., an`, summarize the numbers seen so far as a list of disjoint intervals.

    Implement the `SummaryRanges` class:

    - `SummaryRanges()` Initializes the object with an empty stream.
    - `void addNum(int value)` Adds the integer `value` to the stream.
    - `int[][] getIntervals()` Returns a summary of the integers in the stream currently as a list of disjoint intervals `[starti, endi]`. The answer should be sorted by `starti`.

    ## Examples

    ```
    Input
    ['SummaryRanges', 'addNum', 'getIntervals', 'addNum', 'getIntervals', 'addNum', 'getIntervals', 'addNum', 'getIntervals', 'addNum', 'getIntervals']
    [[], [1], [], [3], [], [7], [], [2], [], [6], []]
    Output
    [None, None, [[1, 1]], None, [[1, 1], [3, 3]], None, [[1, 1], [3, 3], [7, 7]], None, [[1, 3], [7, 7]], None, [[1, 3], [6, 7]]]

    Explanation
    SummaryRanges summaryRanges = new SummaryRanges();
    summaryRanges.addNum(1);      // arr = [1]
    summaryRanges.getIntervals(); // return [[1, 1]]
    summaryRanges.addNum(3);      // arr = [1, 3]
    summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
    summaryRanges.addNum(7);      // arr = [1, 3, 7]
    summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
    summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
    summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
    summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
    summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
    ```

    ## Constraints

    - 0 <= value <= 10<sup>4</sup>
    - At most 3 * 10<sup>4</sup> calls will be made to `addNum` and `getIntervals`.
    - At most 10<sup>2</sup> calls will be made to `getIntervals`.

    **Follow up:** What if there are lots of merges and the number of disjoint intervals is small compared to the size of the data stream?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class SummaryRanges:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def add_num(self, value: int) -> None:
            raise NotImplementedError('Implement add_num')

        def get_intervals(self) -> list[list[int]]:
            raise NotImplementedError('Implement get_intervals')

    practice_exports = {'SummaryRanges': SummaryRanges}
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
