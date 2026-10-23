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
    # 855. Exam Room

    **Medium** · Design, Heap (Priority Queue), Ordered Set

    There is an exam room with `n` seats in a single row labeled from `0` to `n - 1`.

    When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit in the seat with the lowest number. If no one is in the room, then the student sits at seat number `0`.

    Design a class that simulates the mentioned exam room.

    Implement the `ExamRoom` class:

    - `ExamRoom(int n)` Initializes the object of the exam room with the number of the seats `n`.
    - `int seat()` Returns the label of the seat at which the next student will sit.
    - `void leave(int p)` Indicates that the student sitting at seat `p` will leave the room. It is guaranteed that there will be a student sitting at seat `p`.

    ## Examples

    ```
    Input
    ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
    [[10], [], [], [], [], [4], []]
    Output
    [null, 0, 9, 4, 2, null, 5]

    Explanation
    ExamRoom examRoom = new ExamRoom(10);
    examRoom.seat(); // return 0, no one is in the room, then the student sits at seat number 0.
    examRoom.seat(); // return 9, the student sits at the last seat number 9.
    examRoom.seat(); // return 4, the student sits at the last seat number 4.
    examRoom.seat(); // return 2, the student sits at the last seat number 2.
    examRoom.leave(4);
    examRoom.seat(); // return 5, the student sits at the last seat number 5.
    ```

    ## Constraints

    - `1 <= n <= 10^9`
    - It is guaranteed that there is a student sitting at seat `p`.
    - At most `10^4` calls will be made to `seat` and `leave`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class ExamRoom:

        def __init__(self, n: int) -> None:
            raise NotImplementedError('Implement __init__')

        def seat(self) -> int:
            raise NotImplementedError('Implement seat')

        def leave(self, p: int) -> None:
            raise NotImplementedError('Implement leave')

    practice_exports = {'ExamRoom': ExamRoom}
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
