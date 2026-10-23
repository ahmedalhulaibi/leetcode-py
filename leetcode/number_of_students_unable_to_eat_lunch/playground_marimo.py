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
    # 1700. Number of Students Unable to Eat Lunch

    **Easy** · Array, Stack, Queue, Simulation

    The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers `0` and `1` respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

    The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a **stack**. At each step:

    - If the student at the front of the queue **prefers** the sandwich on the top of the stack, they will **take it** and leave the queue.
    - Otherwise, they will **leave it** and go to the queue's end.

    This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

    You are given two integer arrays `students` and `sandwiches` where `sandwiches[i]` is the type of the `i`th sandwich in the stack (`i = 0` is the top of the stack) and `students[j]` is the preference of the `j`th student in the initial queue (`j = 0` is the front of the queue). Return the number of students that are unable to eat.

    ## Examples

    ```
    Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
    Output: 0
    ```
    **Explanation:** Front students who want sandwich `1` move to the end of the queue until the stack exposes `1`, and every student eventually takes a sandwich.

    ```
    Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
    Output: 3
    ```

    ## Constraints

    - 1 <= students.length, sandwiches.length <= 100
    - students.length == sandwiches.length
    - sandwiches[i] is 0 or 1.
    - students[i] is 0 or 1.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_students(self, students: list[int], sandwiches: list[int]) -> int:
            raise NotImplementedError('Implement count_students')

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
