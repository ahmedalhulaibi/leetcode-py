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
    # 2037. Minimum Number of Moves to Seat Everyone

    **Easy** · Array, Greedy, Sorting, Counting Sort

    There are `n` availabe seats and `n` students standing in a room. You are given an array `seats` of length `n`, where `seats[i]` is the position of the `i<sup>th</sup>` seat. You are also given the array `students` of length `n`, where `students[j]` is the position of the `j<sup>th</sup>` student.

    You may perform the following move any number of times:

    - Increase or decrease the position of the `i<sup>th</sup>` student by `1` (i.e., moving the `i<sup>th</sup>` student from position `x` to `x + 1` or `x - 1`)

    Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

    Note that there may be multiple seats or students in the same position at the beginning.

    ## Examples

    ```
    Input: seats = [3,1,5], students = [2,7,4]
    Output: 4
    Explanation: The students are moved as follows:
    - The first student is moved from position 2 to position 1 using 1 move.
    - The second student is moved from position 7 to position 5 using 2 moves.
    - The third student is moved from position 4 to position 3 using 1 move.
    In total, 1 + 2 + 1 = 4 moves were used.
    ```

    ```
    Input: seats = [4,1,5,9], students = [1,3,2,6]
    Output: 7
    Explanation: The students are moved as follows:
    - The first student is not moved.
    - The second student is moved from position 3 to position 4 using 1 move.
    - The third student is moved from position 2 to position 5 using 3 moves.
    - The fourth student is moved from position 6 to position 9 using 3 moves.
    In total, 0 + 1 + 3 + 3 = 7 moves were used.
    ```

    ```
    Input: seats = [2,2,6,6], students = [1,3,2,6]
    Output: 4
    Explanation: Note that there are two seats at position 2 and two seats at position 6.
    The students are moved as follows:
    - The first student is moved from position 1 to position 2 using 1 move.
    - The second student is moved from position 3 to position 6 using 3 moves.
    - The third student is not moved.
    - The fourth student is not moved.
    In total, 1 + 3 + 0 + 0 = 4 moves were used.
    ```

    ## Constraints

    - n == seats.length == students.length
    - 1 <= n <= 100
    - 1 <= seats[i], students[j] <= 100



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_moves_to_seat(self, seats: list[int], students: list[int]) -> int:
            raise NotImplementedError('Implement min_moves_to_seat')

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
