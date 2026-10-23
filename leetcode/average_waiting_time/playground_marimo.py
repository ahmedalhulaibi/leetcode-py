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
    # 1701. Average Waiting Time

    **Medium** · Array, Simulation

    There is a restaurant with a single chef. You are given an array `customers`, where `customers[i] = [arrival<sub>i</sub>, time<sub>i</sub>]`:

    - `arrival<sub>i</sub>` is the arrival time of the `i<sup>th</sup>` customer. The arrival times are sorted in non-decreasing order.
    - `time<sub>i</sub>` is the time needed to prepare the order of the `i<sup>th</sup>` customer.

    When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

    Return *the average waiting time of all customers*. Solutions within `10-5` from the actual answer are considered accepted.

    ## Examples

    ```
    Input: customers = [[1,2],[2,5],[4,3]]
    Output: 5.00000
    Explanation:
    1) The first customer arrives at time 1, the chef takes his order and starts preparing it immediately at time 1, and finishes at time 3, so the waiting time of the first customer is 3 - 1 = 2.
    2) The second customer arrives at time 2, the chef takes his order and starts preparing it at time 3, and finishes at time 8, so the waiting time of the second customer is 8 - 2 = 6.
    3) The third customer arrives at time 4, the chef takes his order and starts preparing it at time 8, and finishes at time 11, so the waiting time of the third customer is 11 - 4 = 7.
    So the average waiting time = (2 + 6 + 7) / 3 = 5.
    ```

    ```
    Input: customers = [[5,2],[5,4],[10,3],[20,1]]
    Output: 3.25000
    Explanation:
    1) The first customer arrives at time 5, the chef takes his order and starts preparing it immediately at time 5, and finishes at time 7, so the waiting time of the first customer is 7 - 5 = 2.
    2) The second customer arrives at time 5, the chef takes his order and starts preparing it at time 7, and finishes at time 11, so the waiting time of the second customer is 11 - 5 = 6.
    3) The third customer arrives at time 10, the chef takes his order and starts preparing it at time 11, and finishes at time 14, so the waiting time of the third customer is 14 - 10 = 4.
    4) The fourth customer arrives at time 20, the chef takes his order and starts preparing it immediately at time 20, and finishes at time 21, so the waiting time of the fourth customer is 21 - 20 = 1.
    So the average waiting time = (2 + 6 + 4 + 1) / 4 = 3.25.
    ```

    ## Constraints

    - 1 <= customers.length <= 10^5
    - 1 <= arrival<sub>i</sub>, time<sub>i</sub> <= 10^4
    - arrival<sub>i</sub> <= arrival<sub>i+1</sub>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def average_waiting_time(self, customers: list[list[int]]) -> float:
            raise NotImplementedError('Implement average_waiting_time')

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
