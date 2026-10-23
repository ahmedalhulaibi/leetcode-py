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
    # 351. Android Unlock Patterns

    **Medium** · Bit Manipulation, Dynamic Programming, Backtracking, Bitmask

    Android devices have a special lock screen with a `3 x 3` grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, forming a series of joined line segments where each segment's endpoints are two consecutive dots in the sequence. A sequence of `k` dots is a **valid** unlock pattern if both of the following are true:

    - All the dots in the sequence are **distinct**.
    - If the line segment connecting two consecutive dots in the sequence passes through the **center** of any other dot, the other dot **must have previously appeared** in the sequence. No jumps through the center non-selected dots are allowed.
        - For example, connecting dots `2` and `9` without dots `5` or `6` appearing beforehand is valid because the line from dot `2` to dot `9` does not pass through the center of either dot `5` or `6`.
        - However, connecting dots `1` and `3` without dot `2` appearing beforehand is invalid because the line from dot `1` to dot `3` passes through the center of dot `2`.

    Given two integers `m` and `n`, return *the **number of unique and valid unlock patterns** of the Android grid lock screen that consist of **at least*** `m` *keys and **at most*** `n` *keys*.

    Two unlock patterns are considered **unique** if there is a dot in one sequence that is not in the other, or the order of the dots is different.

    ## Examples

    ![Unlock patterns](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0351.Android%20Unlock%20Patterns/images/android-unlock.png)

    ```
    Input: m = 1, n = 1
    Output: 9
    ```

    ```
    Input: m = 1, n = 2
    Output: 65
    ```

    ## Constraints

    - `1 <= m, n <= 9`
    - `m <= n`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def number_of_patterns(self, m: int, n: int) -> int:
            raise NotImplementedError('Implement number_of_patterns')

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
