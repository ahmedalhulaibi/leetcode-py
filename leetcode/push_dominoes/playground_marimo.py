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
    # 838. Push Dominoes

    **Medium** · Two Pointers, String, Dynamic Programming

    There are `n` dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

    After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

    When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

    For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

    You are given a string `dominoes` representing the initial state where:

    - `dominoes[i] = 'L'`, if the `ith` domino has been pushed to the left,
    - `dominoes[i] = 'R'`, if the `ith` domino has been pushed to the right, and
    - `dominoes[i] = '.'`, if the `ith` domino has not been pushed.

    Return *a string representing the final state*.

    ## Examples

    ```
    Input: dominoes = "RR.L"
    Output: "RR.L"
    Explanation: The first domino expends no additional force on the second domino.
    ```

    ```
    Input: dominoes = ".L.R...LR..L.."
    Output: "LL.RR.LLRRLL.."
    ```

    ## Constraints

    - n == dominoes.length
    - 1 <= n <= 10^5
    - dominoes[i] is either 'L', 'R', or '.'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def push_dominoes(self, dominoes: str) -> str:
            raise NotImplementedError('Implement push_dominoes')

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
