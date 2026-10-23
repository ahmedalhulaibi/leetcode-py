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
    # 914. X of a Kind in a Deck of Cards

    **Easy** · Array, Hash Table, Math, Counting, Number Theory, Euclidean Algorithm, Greatest Common Divisor

    You are given an integer array `deck` where `deck[i]` represents the number written on the `i^th` card.

    Partition the cards into one or more groups such that:

    - Each group has **exactly** `x` cards where `x > 1`, and
    - All the cards in one group have the same integer written on them.

    Return `true` if such partition is possible, or `false` otherwise.

    ## Examples

    ```
    Input: deck = [1,2,3,4,4,3,2,1]
    Output: true
    ```
    **Explanation:** Possible partition `[1,1],[2,2],[3,3],[4,4]`.

    ```
    Input: deck = [1,1,1,2,2,2,3,3]
    Output: false
    ```
    **Explanation:** No possible partition.

    ## Constraints

    - 1 <= deck.length <= 10^4
    - 0 <= deck[i] < 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def has_group_size_x(self, deck: list[int]) -> bool:
            raise NotImplementedError('Implement has_group_size_x')

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
