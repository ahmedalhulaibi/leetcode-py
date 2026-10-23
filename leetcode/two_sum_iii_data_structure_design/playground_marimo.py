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
    # 170. Two Sum III - Data structure design

    **Easy** · Design, Array, Hash Table, Two Pointers, Data Stream

    Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

    Implement the `TwoSum` class:

    - `TwoSum()` Initializes the `TwoSum` object, with an empty array initially.
    - `void add(int number)` Adds `number` to the data structure.
    - `boolean find(int value)` Returns `true` if there exists any pair of numbers whose sum is equal to `value`, otherwise, it returns `false`.

    ## Examples

    ```
    Input
    ["TwoSum", "add", "add", "add", "find", "find"]
    [[], [1], [3], [5], [4], [7]]
    Output
    [null, null, null, null, true, false]

    Explanation
    TwoSum twoSum = new TwoSum();
    twoSum.add(1);
    twoSum.add(3);
    twoSum.add(5);
    twoSum.find(4); // 1 + 3 = 4, return true
    twoSum.find(7); // No two integers sum up to 7, return false
    ```

    ## Constraints

    - `-10^5 <= number <= 10^5`
    - `-2^31 <= value <= 2^31 - 1`
    - At most `10^4` calls will be made to `add` and `find`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class TwoSum:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def add(self, number: int) -> None:
            raise NotImplementedError('Implement add')

        def find(self, value: int) -> bool:
            raise NotImplementedError('Implement find')

    practice_exports = {'TwoSum': TwoSum}
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
