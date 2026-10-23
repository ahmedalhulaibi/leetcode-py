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
    # 956. Tallest Billboard

    **Hard** · Array, Dynamic Programming, Meet in the Middle, Knapsack Problem, 0-1 Knapsack

    You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

    You are given a collection of `rods` that can be welded together. For example, if you have rods of lengths `1`, `2`, and `3`, you can weld them together to make a support of length `6`.

    Return the largest possible height of your billboard installation. If you cannot support the billboard, return `0`.

    ## Examples

    ```
    Input: rods = [1,2,3,6]
    Output: 6
    ```
    **Explanation:** We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.

    ```
    Input: rods = [1,2,3,4,5,6]
    Output: 10
    ```
    **Explanation:** We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.

    ```
    Input: rods = [1,2]
    Output: 0
    ```
    **Explanation:** The billboard cannot be supported, so we return 0.

    ## Constraints

    - 1 <= rods.length <= 20
    - 1 <= rods[i] <= 1000
    - sum(rods[i]) <= 5000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def tallest_billboard(self, rods: list[int]) -> int:
            raise NotImplementedError('Implement tallest_billboard')

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
