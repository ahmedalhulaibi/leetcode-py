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
    # 1845. Seat Reservation Manager

    **Medium** · Design, Heap (Priority Queue)

    Design a system that manages the reservation state of `n` seats that are numbered from `1` to `n`.

    Implement the `SeatManager` class:

    - `SeatManager(int n)` Initializes a `SeatManager` object that will manage `n` seats numbered from `1` to `n`. All seats are initially available.
    - `int reserve()` Fetches the **smallest-numbered** unreserved seat, reserves it, and returns its number.
    - `void unreserve(int seatNumber)` Unreserves the seat with the given `seatNumber`.

    ## Examples

    ```
    Input
    ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
    [[5], [], [], [2], [], [], [], [], [5]]
    Output
    [null, 1, 2, null, 2, 3, 4, 5, null]

    Explanation
    SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
    seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
    seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
    seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
    seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
    seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
    seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
    seatManager.reserve();    // The only available seat is seat 5, so return 5.
    seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].
    ```

    ## Constraints

    - `1 <= n <= 10^5`
    - `1 <= seatNumber <= n`
    - For each call to `reserve`, it is guaranteed that there will be at least one unreserved seat.
    - For each call to `unreserve`, it is guaranteed that `seatNumber` will be reserved.
    - At most `10^5` calls in total will be made to `reserve` and `unreserve`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class SeatManager:

        def __init__(self, n: int) -> None:
            raise NotImplementedError('Implement __init__')

        def reserve(self) -> int:
            raise NotImplementedError('Implement reserve')

        def unreserve(self, seat_number: int) -> None:
            raise NotImplementedError('Implement unreserve')

    practice_exports = {'SeatManager': SeatManager}
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
