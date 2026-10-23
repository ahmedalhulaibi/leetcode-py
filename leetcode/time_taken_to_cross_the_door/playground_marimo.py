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
    mo.md(r"""
    # 2534. Time Taken to Cross the Door

    **Hard** · Queue, Array, Simulation

    There are <code>n</code> persons numbered from <code>0</code> to <code>n - 1</code> and a door. Each person can enter or exit through the door once, taking one second.</p>

    <p>You are given a <strong>non-decreasing</strong> integer array <code>arrival</code> of size <code>n</code>, where <code>arrival[i]</code> is the arrival time of the <code>i<sup>th</sup></code> person at the door. You are also given an array <code>state</code> of size <code>n</code>, where <code>state[i]</code> is <code>0</code> if person <code>i</code> wants to enter through the door or <code>1</code> if they want to exit through the door.</p>

    <p>If two or more persons want to use the door at the <strong>same</strong> time, they follow the following rules:</p>

    <ul>
        <li>If the door was <strong>not</strong> used in the previous second, then the person who wants to <strong>exit</strong> goes first.</li>
        <li>If the door was used in the previous second for <strong>entering</strong>, the person who wants to enter goes first.</li>
        <li>If the door was used in the previous second for <strong>exiting</strong>, the person who wants to <strong>exit</strong> goes first.</li>
        <li>If multiple persons want to go in the same direction, the person with the <strong>smallest</strong> index goes first.</li>
    </ul>

    <p>Return <em>an array </em><code>answer</code><em> of size </em><code>n</code><em> where </em><code>answer[i]</code><em> is the second at which the <code>i<sup>th</sup></code> person crosses the door</em>.</p>

    <p><strong>Note</strong> that:</p>

    <ul>
        <li>Only one person can cross the door at each second.</li>
        <li>A person may arrive at the door and wait without entering or exiting to follow the mentioned rules.</li>
    </ul>

    ## Examples

    ```
    Input: arrival = [0,1,1,2,4], state = [0,1,0,0,1]
    Output: [0,3,1,2,4]
    Explanation: At each second we have the following:
    - At t = 0: Person 0 is the only one who wants to enter, so they just enter through the door.
    - At t = 1: Person 1 wants to exit, and person 2 wants to enter. Since the door was used the previous second for entering, person 2 enters.
    - At t = 2: Person 1 still wants to exit, and person 3 wants to enter. Since the door was used the previous second for entering, person 3 enters.
    - At t = 3: Person 1 is the only one who wants to exit, so they just exit through the door.
    - At t = 4: Person 4 is the only one who wants to exit, so they just exit through the door.
    ```

    ```
    Input: arrival = [0,0,0], state = [1,0,1]
    Output: [0,2,1]
    Explanation: At each second we have the following:
    - At t = 0: Person 1 wants to enter while persons 0 and 2 want to exit. Since the door was not used in the previous second, the persons who want to exit get to go first. Since person 0 has a smaller index, they exit first.
    - At t = 1: Person 1 wants to enter, and person 2 wants to exit. Since the door was used in the previous second for exiting, person 2 exits.
    - At t = 2: Person 1 is the only one who wants to enter, so they just enter through the door.
    ```

    ## Constraints

    - n == arrival.length == state.length
    - 1 <= n <= 10^5
    - 0 <= arrival[i] <= n
    - arrival is sorted in non-decreasing order.
    - state[i] is either 0 or 1.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def time_taken(self, arrival: list[int], state: list[int]) -> list[int]:
            raise NotImplementedError('Implement time_taken')

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
