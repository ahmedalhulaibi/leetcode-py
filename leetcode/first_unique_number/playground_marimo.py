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
    # 1429. First Unique Number

    **Medium** · Design, Queue, Array, Hash Table, Data Stream

    You have a queue of integers, you need to retrieve the first unique integer in the queue.

    Implement the `FirstUnique` class:

    - `FirstUnique(int[] nums)` Initializes the object with the numbers in the queue.
    - `int showFirstUnique()` returns the value of **the first unique** integer of the queue, and returns **-1** if there is no such integer.
    - `void add(int value)` insert value to the queue.

    ## Examples

    ```
    Input
    ["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"]
    [[[2, 3, 5]], [], [5], [], [2], [], [3], []]
    Output
    [null, 2, null, 2, null, 3, null, -1]
    ```

    ```
    Input
    ["FirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique"]
    [[[7, 7, 7, 7, 7, 7]], [], [7], [3], [3], [7], [17], []]
    Output
    [null, -1, null, null, null, null, null, 17]
    ```

    ```
    Input
    ["FirstUnique", "showFirstUnique", "add", "showFirstUnique"]
    [[[809]], [], [809], []]
    Output
    [null, 809, null, -1]
    ```

    ## Constraints

    - `1 <= nums.length <= 10^5`
    - `1 <= nums[i] <= 10^8`
    - `1 <= value <= 10^8`
    - At most `50000` calls will be made to `showFirstUnique` and `add`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class FirstUnique:

        def __init__(self, nums: list[int]) -> None:
            raise NotImplementedError('Implement __init__')

        def show_first_unique(self) -> int:
            raise NotImplementedError('Implement show_first_unique')

        def add(self, value: int) -> None:
            raise NotImplementedError('Implement add')

    practice_exports = {'FirstUnique': FirstUnique}
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
