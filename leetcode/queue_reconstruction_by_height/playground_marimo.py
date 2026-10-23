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
    # 406. Queue Reconstruction by Height

    **Medium** · Array, Binary Indexed Tree, Segment Tree, Sorting

    You are given an array of people, `people`, which are the attributes of some people in a queue (not necessarily in order). Each `people[i] = [h<sub>i</sub>, k<sub>i</sub>]` represents the i<sup>th</sup> person of height `h<sub>i</sub>` with exactly `k<sub>i</sub>` other people in front who have a height greater than or equal to `h<sub>i</sub>`.

    Reconstruct and return the queue that is represented by the input array `people`. The returned queue should be formatted as an array `queue`, where `queue[j] = [h<sub>j</sub>, k<sub>j</sub>]` is the attributes of the j<sup>th</sup> person in the queue (`queue[0]` is the person at the front of the queue).

    ## Examples

    ```
    Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    ```
    **Explanation:**
    - Person 0 has height 5 with no other people taller or the same height in front.
    - Person 1 has height 7 with no other people taller or the same height in front.
    - Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
    - Person 3 has height 6 with one person taller or the same height in front, which is person 1.
    - Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
    - Person 5 has height 7 with one person taller or the same height in front, which is person 1.
    Hence `[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]` is the reconstructed queue.

    ```
    Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
    Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
    ```

    ## Constraints

    - `1 <= people.length <= 2000`
    - `0 <= h<sub>i</sub> <= 10^6`
    - `0 <= k<sub>i</sub> < people.length`
    - It is guaranteed that the queue can be reconstructed.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def reconstruct_queue(self, people: list[list[int]]) -> list[list[int]]:
            raise NotImplementedError('Implement reconstruct_queue')

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
