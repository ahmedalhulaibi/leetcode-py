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
    # 390. Elimination Game

    **Medium** · Math, Recursion

    You have a list <code>arr</code> of all integers in the range <code>[1, n]</code> sorted in a strictly increasing order. Apply the following algorithm on <code>arr</code>:

    <ul>
        <li>Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.</li>
        <li>Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.</li>
        <li>Keep repeating the steps again, alternating left to right and right to left, until a single number remains.</li>
    </ul>

    <p>Given the integer <code>n</code>, return <em>the last number that remains in</em> <code>arr</code>.</p>

    ## Examples

    ```
    Input: n = 9
    Output: 6
    Explanation:
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr = [2, 4, 6, 8]
    arr = [2, 6]
    arr = [6]
    ```

    ```
    Input: n = 1
    Output: 1
    ```

    ## Constraints

    - 1 <= n <= 10<sup>9</sup>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def last_remaining(self, n: int) -> int:
            raise NotImplementedError('Implement last_remaining')

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
