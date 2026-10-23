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
    # 362. Design Hit Counter

    **Medium** · Design, Queue, Array, Binary Search, Data Stream

    Design a hit counter which counts the number of hits received in the past `5` minutes (i.e., the past `300` seconds).

    Your system should accept a `timestamp` parameter (**in seconds** granularity), and you may assume that calls are being made to the system in chronological order (i.e., `timestamp` is monotonically increasing). Several hits may arrive roughly at the same time.

    Implement the `HitCounter` class:

    - `HitCounter()` Initializes the object of the hit counter system.
    - `void hit(int timestamp)` Records a hit that happened at `timestamp` (**in seconds**). Several hits may happen at the same `timestamp`.
    - `int getHits(int timestamp)` Returns the number of hits in the past 5 minutes from `timestamp` (i.e., the past `300` seconds).

    ## Examples

    ```
    Input
    ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
    [[], [1], [2], [3], [4], [300], [300], [301]]
    Output
    [null, null, null, null, 3, null, 4, 3]

    Explanation
    HitCounter hitCounter = new HitCounter();
    hitCounter.hit(1);       // hit at timestamp 1.
    hitCounter.hit(2);       // hit at timestamp 2.
    hitCounter.hit(3);       // hit at timestamp 3.
    hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
    hitCounter.hit(300);     // hit at timestamp 300.
    hitCounter.getHits(300); // get hits at timestamp 300, return 4.
    hitCounter.getHits(301); // get hits at timestamp 301, return 3.
    ```

    ## Constraints

    - `1 <= timestamp <= 2 * 10^9`
    - All the calls are being made to the system in chronological order (i.e., `timestamp` is monotonically increasing).
    - At most `300` calls will be made to `hit` and `getHits`.

    **Follow up:** What if the number of hits per second could be huge? Does your design scale?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class HitCounter:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def hit(self, timestamp: int) -> None:
            raise NotImplementedError('Implement hit')

        def get_hits(self, timestamp: int) -> int:
            raise NotImplementedError('Implement get_hits')

    practice_exports = {'HitCounter': HitCounter}
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
