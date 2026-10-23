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
    # 526. Beautiful Arrangement

    **Medium** · Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask

    Suppose you have `n` integers labeled `1` through `n`. A permutation of those `n` integers `perm` (**1-indexed**) is considered a **beautiful arrangement** if for every `i` (`1 <= i <= n`), **either** of the following is true:

    - `perm[i]` is divisible by `i`.
    - `i` is divisible by `perm[i]`.

    Given an integer `n`, return *the **number** of the **beautiful arrangements** that you can construct*.

    ## Examples

    ```
    Input: n = 2
    Output: 2
    Explanation:
    The first beautiful arrangement is [1,2]:
        - perm[1] = 1 is divisible by i = 1
        - perm[2] = 2 is divisible by i = 2
    The second beautiful arrangement is [2,1]:
        - perm[1] = 2 is divisible by i = 1
        - i = 2 is divisible by perm[2] = 1
    ```

    ```
    Input: n = 1
    Output: 1
    ```

    ## Constraints

    - `1 <= n <= 15`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_arrangement(self, n: int) -> int:
            raise NotImplementedError('Implement count_arrangement')

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
