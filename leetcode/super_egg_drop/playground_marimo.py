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
    # 887. Super Egg Drop

    **Hard** · Math, Binary Search, Dynamic Programming

    You are given `k` identical eggs and you have access to a building with `n` floors labeled from `1` to `n`.

    You know that there exists a floor `f` where `0 <= f <= n` such that any egg dropped at a floor **higher** than `f` will **break**, and any egg dropped **at or below** floor `f` will **not break**.

    Each move, you may take an unbroken egg and drop it from any floor `x` (where `1 <= x <= n`). If the egg breaks, you can no longer use it. However, if the egg does not break, you may **reuse** it in future moves.

    Return *the **minimum number of moves** that you need to determine **with certainty** what the value of* `f` *is*.

    ## Examples

    ```
    Input: k = 1, n = 2
    Output: 2
    Explanation:
    Drop the egg from floor 1. If it breaks, we know that f = 0.
    Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
    If it does not break, then we know f = 2.
    Hence, we need at minimum 2 moves to determine with certainty what the value of f is.
    ```

    ```
    Input: k = 2, n = 6
    Output: 3
    ```

    ```
    Input: k = 3, n = 14
    Output: 4
    ```

    ## Constraints

    - 1 <= k <= 100
    - 1 <= n <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def super_egg_drop(self, k: int, n: int) -> int:
            raise NotImplementedError('Implement super_egg_drop')

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
