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
    # 2073. Time Needed to Buy Tickets

    **Easy** · Array, Queue, Simulation

    There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

    You are given a 0-indexed integer array `tickets` of length n where the number of tickets that the ith person would like to buy is `tickets[i]`.

    Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

    Return the time taken for the person initially at position k (0-indexed) to finish buying tickets.

    ## Examples

    ```
    Input: tickets = [2,3,2], k = 2
    Output: 6
    ```
    **Explanation:**

    - The queue starts as [2,3,2], where the kth person is underlined.
    - After the person at the front has bought a ticket, the queue becomes [3,2,1] at 1 second.
    - Continuing this process, the queue becomes [2,1,2] at 2 seconds.
    - Continuing this process, the queue becomes [1,2,1] at 3 seconds.
    - Continuing this process, the queue becomes [2,1] at 4 seconds. Note: the person at the front left the queue.
    - Continuing this process, the queue becomes [1,1] at 5 seconds.
    - Continuing this process, the queue becomes [1] at 6 seconds. The kth person has bought all their tickets, so return 6.

    ```
    Input: tickets = [5,1,1,1], k = 0
    Output: 8
    ```
    **Explanation:**

    - The queue starts as [5,1,1,1], where the kth person is underlined.
    - After the person at the front has bought a ticket, the queue becomes [1,1,1,4] at 1 second.
    - Continuing this process for 3 seconds, the queue becomes [4] at 4 seconds.
    - Continuing this process for 4 seconds, the queue becomes [] at 8 seconds. The kth person has bought all their tickets, so return 8.

    ## Constraints

    - n == tickets.length
    - 1 <= n <= 100
    - 1 <= tickets[i] <= 100
    - 0 <= k < n



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def time_required_to_buy(self, tickets: list[int], k: int) -> int:
            raise NotImplementedError('Implement time_required_to_buy')

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
