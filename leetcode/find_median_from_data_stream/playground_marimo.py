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
    # 295. Find Median from Data Stream

    **Hard** · Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream

    The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

    - For example, for `arr = [2,3,4]`, the median is `3`.
    - For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

    Implement the MedianFinder class:

    - `MedianFinder()` initializes the `MedianFinder` object.
    - `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
    - `double findMedian()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

    ## Examples

    ```
    Input
    ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    [[], [1], [2], [], [3], []]
    Output
    [null, null, null, 1.5, null, 2.0]
    ```

    **Explanation:**
    ```
    MedianFinder medianFinder = new MedianFinder();
    medianFinder.addNum(1);    // arr = [1]
    medianFinder.addNum(2);    // arr = [1, 2]
    medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3);    // arr = [1, 2, 3]
    medianFinder.findMedian(); // return 2.0
    ```

    ## Constraints

    - `-10^5 <= num <= 10^5`
    - There will be at least one element in the data structure before calling `findMedian`.
    - At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.

    **Follow up:**

    - If all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?
    - If `99%` of all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class MedianFinder:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def add_num(self, num: int) -> None:
            raise NotImplementedError('Implement add_num')

        def find_median(self) -> float:
            raise NotImplementedError('Implement find_median')

    practice_exports = {'MedianFinder': MedianFinder}
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
