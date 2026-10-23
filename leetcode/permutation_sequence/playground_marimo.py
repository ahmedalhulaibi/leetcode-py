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
    # 60. Permutation Sequence

    **Hard** · Math, Recursion

    The set `[1, 2, 3, ..., n]` contains a total of `n!` unique permutations.

    By listing and labeling all of the permutations in order, we get the following sequence for `n = 3`:

    - `"123"`
    - `"132"`
    - `"213"`
    - `"231"`
    - `"312"`
    - `"321"`

    Given `n` and `k`, return the `kth` permutation sequence.

    ## Examples

    ```
    Input: Input: n = 3, k = 3
    Output: "213"
    ```

    ```
    Input: Input: n = 4, k = 9
    Output: "2314"
    ```

    ```
    Input: Input: n = 3, k = 1
    Output: "123"
    ```

    ## Constraints

    - `1 <= n <= 9`
    - `1 <= k <= n!`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def get_permutation(self, n: int, k: int) -> str:
            raise NotImplementedError('Implement get_permutation')

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
