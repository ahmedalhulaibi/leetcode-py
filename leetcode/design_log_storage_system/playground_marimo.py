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
    # 635. Design Log Storage System

    **Medium** · Design, Hash Table, String, Ordered Set

    You are given several logs, where each log contains a unique ID and timestamp. Timestamp is a string that has the following format: `Year:Month:Day:Hour:Minute:Second`, for example, `2017:01:01:23:59:59`. All domains are zero-padded decimal numbers.

    Implement the `LogSystem` class:

    - `LogSystem()` Initializes the `LogSystem` object.
    - `void put(int id, string timestamp)` Stores the given log `(id, timestamp)` in your storage system.
    - `int[] retrieve(string start, string end, string granularity)` Returns the IDs of the logs whose timestamps are within the range from `start` to `end` inclusive. `start` and `end` all have the same format as `timestamp`, and `granularity` means how precise the range should be (i.e. to the exact `Day`, `Minute`, etc.).

    ## Examples

    ```
    Input
    ["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
    [[1, "2017:01:01:23:59:59"], ...]
    Output
    [null, null, null, null, [3, 2, 1], [2, 1]]

    Explanation
    LogSystem logSystem = new LogSystem();
    logSystem.put(1, "2017:01:01:23:59:59");
    logSystem.put(2, "2017:01:01:22:59:59");
    log.put(3, "2016:01:01:00:00:00");
    logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"); // return [3,2,1], all logs between 2016 and 2017.
    logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"); // return [2,1]
    ```

    ## Constraints

    - `1 <= id <= 500`
    - `2000 <= Year <= 2017`
    - `1 <= Month <= 12`
    - `1 <= Day <= 31`
    - `0 <= Hour <= 23`
    - `0 <= Minute, Second <= 59`
    - `granularity` is one of the values `["Year", "Month", "Day", "Hour", "Minute", "Second"]`.
    - At most `500` calls will be made to `put` and `retrieve`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class LogSystem:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def put(self, log_id: int, timestamp: str) -> None:
            raise NotImplementedError('Implement put')

        def retrieve(self, start: str, end: str, granularity: str) -> list[int]:
            raise NotImplementedError('Implement retrieve')

    practice_exports = {'LogSystem': LogSystem}
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
