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
    # 379. Design Phone Directory

    **Medium** · Design, Queue, Array, Hash Table, Linked List

    Design a phone directory that initially has `maxNumbers` empty slots that can store numbers. The directory should store numbers, check if a certain slot is empty or not, and empty a given slot.

    Implement the `PhoneDirectory` class:

    - `PhoneDirectory(int maxNumbers)` Initializes the phone directory with the number of available slots `maxNumbers`.
    - `int get()` Provides a number that is not assigned to anyone. Returns `-1` if no number is available.
    - `bool check(int number)` Returns `true` if the slot `number` is available and `false` otherwise.
    - `void release(int number)` Recycles or releases the slot `number`.

    ## Examples

    ```
    Input
    ["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
    [[3], [], [], [2], [], [2], [2], [2]]
    Output
    [null, 0, 1, true, 2, false, null, true]

    Explanation
    PhoneDirectory phoneDirectory = new PhoneDirectory(3);
    phoneDirectory.get();      // It can return any available phone number. Here we assume it returns 0.
    phoneDirectory.get();      // Assume it returns 1.
    phoneDirectory.check(2);   // The number 2 is available, so return true.
    phoneDirectory.get();      // It returns 2, the only number that is left.
    phoneDirectory.check(2);   // The number 2 is no longer available, so return false.
    phoneDirectory.release(2); // Release number 2 back to the pool.
    phoneDirectory.check(2);   // Number 2 is available again, return true.
    ```

    ## Constraints

    - `1 <= maxNumbers <= 10^4`
    - `0 <= number < maxNumbers`
    - At most `2 * 10^4` calls will be made to `get`, `check`, and `release`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class PhoneDirectory:

        def __init__(self, max_numbers: int) -> None:
            raise NotImplementedError('Implement __init__')

        def get(self) -> int:
            raise NotImplementedError('Implement get')

        def check(self, number: int) -> bool:
            raise NotImplementedError('Implement check')

        def release(self, number: int) -> None:
            raise NotImplementedError('Implement release')

    practice_exports = {'PhoneDirectory': PhoneDirectory}
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
