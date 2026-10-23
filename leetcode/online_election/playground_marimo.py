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
    # 911. Online Election

    **Medium** · Array, Hash Table, Binary Search, Design

    You are given two integer arrays `persons` and `times`. In an election, the `i-th` vote was cast for `persons[i]` at time `times[i]`.

    For each query at a time `t`, find the person that was leading the election at time `t`. Votes cast at time `t` will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

    Implement the `TopVotedCandidate` class:

    - `TopVotedCandidate(int[] persons, int[] times)` Initializes the object with the `persons` and `times` arrays.
    - `int q(int t)` Returns the number of the person that was leading the election at time `t` according to the mentioned rules.

    ## Examples

    ```
    Input
    ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
    [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
    Output
    [null, 0, 1, 1, 0, 0, 1]

    Explanation
    TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
    topVotedCandidate.q(3); // return 0, At time 3, the votes are [0], and 0 is leading.
    topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and 1 is leading.
    topVotedCandidate.q(25); // return 1, At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
    topVotedCandidate.q(15); // return 0
    topVotedCandidate.q(24); // return 0
    topVotedCandidate.q(8); // return 1
    ```

    ## Constraints

    - `1 <= persons.length <= 5000`
    - `times.length == persons.length`
    - `0 <= persons[i] < persons.length`
    - `0 <= times[i] <= 10^9`
    - `times` is sorted in a strictly increasing order.
    - `times[0] <= t <= 10^9`
    - At most `10^4` calls will be made to `q`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class TopVotedCandidate:

        def __init__(self, persons: list[int], times: list[int]) -> None:
            raise NotImplementedError('Implement __init__')

        def q(self, t: int) -> int:
            raise NotImplementedError('Implement q')

    practice_exports = {'TopVotedCandidate': TopVotedCandidate}
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
