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
    # 1769. Minimum Number of Operations to Move All Balls to Each Box

    **Medium** · Array, String, Prefix Sum

    <p>You have <code>n</code> boxes. You are given a binary string <code>boxes</code> of length <code>n</code>, where <code>boxes[i]</code> is <code>'0'</code> if the <code>i<sup>th</sup></code> box is <strong>empty</strong>, and <code>'1'</code> if it contains <strong>one</strong> ball.</p>

    <p>In one operation, you can move <strong>one</strong> ball from a box to an adjacent box. Box <code>i</code> is adjacent to box <code>j</code> if <code>abs(i - j) == 1</code>. Note that after doing so, there may be more than one ball in some boxes.</p>

    <p>Return an array <code>answer</code> of size <code>n</code>, where <code>answer[i]</code> is the <strong>minimum</strong> number of operations needed to move all the balls to the <code>i<sup>th</sup></code> box.</p>

    <p>Each <code>answer[i]</code> is calculated considering the <strong>initial</strong> state of the boxes.</p>

    ## Examples

    ```
    Input: boxes = "110"
    Output: [1,1,3]
    Explanation: The answer for each box is as follows:
    1) First box: you will have to move one ball from the second box to the first box in one operation.
    2) Second box: you will have to move one ball from the first box to the second box in one operation.
    3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
    ```

    ```
    Input: boxes = "001011"
    Output: [11,8,5,4,3,4]
    ```

    ## Constraints

    - n == boxes.length
    - 1 <= n <= 2000
    - boxes[i] is either '0' or '1'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_operations(self, boxes: str) -> list[int]:
            raise NotImplementedError('Implement min_operations')

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
