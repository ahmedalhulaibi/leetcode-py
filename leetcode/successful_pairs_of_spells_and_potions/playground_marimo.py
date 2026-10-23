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
    # 2300. Successful Pairs of Spells and Potions

    **Medium** · Array, Two Pointers, Binary Search, Sorting

    You are given two positive integer arrays `spells` and `potions`, of length `n` and `m` respectively, where `spells[i]` represents the strength of the `i`th spell and `potions[j]` represents the strength of the `j`th potion.

    You are also given an integer `success`. A spell and potion pair is considered **successful** if the **product** of their strengths is **at least** `success`.

    Return *an integer array* `pairs` *of length* `n` *where* `pairs[i]` *is the number of **potions** that will form a successful pair with the* `i`th *spell.*

    ## Examples

    ```
    Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
    Output: [4,0,3]
    Explanation:
    - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
    - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
    - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
    Thus, [4,0,3] is returned.
    ```

    ```
    Input: spells = [3,1,2], potions = [8,5,8], success = 16
    Output: [2,0,2]
    Explanation:
    - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
    - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful.
    - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful.
    Thus, [2,0,2] is returned.
    ```

    ## Constraints

    - n == spells.length
    - m == potions.length
    - 1 <= n, m <= 10^5
    - 1 <= spells[i], potions[i] <= 10^5
    - 1 <= success <= 10^10



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def successful_pairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
            raise NotImplementedError('Implement successful_pairs')

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
