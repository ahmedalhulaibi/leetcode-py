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
    # 1942. The Number of the Smallest Unoccupied Chair

    **Medium** · Array, Hash Table, Heap (Priority Queue)

    There is a party where `n` friends numbered from `0` to `n - 1` are attending. There is an infinite number of chairs in this party that are numbered from `0` to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

    For example, if chairs `0`, `1`, and `5` are occupied when a friend comes, they will sit on chair number `2`.

    When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

    You are given a 0-indexed 2D integer array `times` where `times[i] = [arrival<sub>i</sub>, leaving<sub>i</sub>]`, indicating the arrival and leaving times of the i<sup>th</sup> friend respectively, and an integer `targetFriend`. All arrival times are distinct.

    Return the chair number that the friend numbered `targetFriend` will sit on.

    ## Examples

    ```
    Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
    Output: 1
    Explanation:
    - Friend 0 arrives at time 1 and sits on chair 0.
    - Friend 1 arrives at time 2 and sits on chair 1.
    - Friend 1 leaves at time 3 and chair 1 becomes empty.
    - Friend 0 leaves at time 4 and chair 0 becomes empty.
    - Friend 2 arrives at time 4 and sits on chair 0.
    Since friend 1 sat on chair 1, we return 1.
    ```

    ```
    Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
    Output: 2
    Explanation:
    - Friend 1 arrives at time 1 and sits on chair 0.
    - Friend 2 arrives at time 2 and sits on chair 1.
    - Friend 0 arrives at time 3 and sits on chair 2.
    - Friend 1 leaves at time 5 and chair 0 becomes empty.
    - Friend 2 leaves at time 6 and chair 1 becomes empty.
    - Friend 0 leaves at time 10 and chair 2 becomes empty.
    Since friend 0 sat on chair 2, we return 2.
    ```

    ## Constraints

    - n == times.length
    - 2 <= n <= 10^4
    - times[i].length == 2
    - 1 <= arrivali < leavingi <= 10^5
    - 0 <= targetFriend <= n - 1
    - Each arrivali time is distinct.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def smallest_chair(self, times: list[list[int]], target_friend: int) -> int:
            raise NotImplementedError('Implement smallest_chair')

    practice_exports = {'Solution': Solution}
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
