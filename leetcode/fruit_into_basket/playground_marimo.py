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
    # 904. Fruit Into Baskets

    **Medium** · Array, Hash Table, Sliding Window

    You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array <code>fruits</code> where <code>fruits[i]</code> is the <strong>type</strong> of fruit the <code>i<sup>th</sup></code> tree produces. You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:</p>

    <ul>
        <li>You only have <strong>two</strong> baskets, and each basket can only hold a <strong>single type</strong> of fruit. There is no limit on the amount of fruit each basket can hold.</li>
        <li>Starting from any tree of your choice, you must pick exactly <strong>one fruit</strong> from <strong>every</strong> tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.</li>
        <li>Once you get to a tree, the fruit cannot jump back to the tree 1. (For example, if you pick fruit 1 from tree 2, you cannot pick fruit 1 from tree 1.)</li>
        <li>Given the integer array <code>fruits</code>, return <em>the <strong>maximum</strong> number of fruits you can pick.</em></li>
    </ul>

    ## Examples

    ```
    Input: fruits = [1,2,1]
    Output: 3
    Explanation: We can pick from all 3 trees.
    ```

    ```
    Input: fruits = [0,1,2,2]
    Output: 3
    Explanation: We can pick from trees [1,2,2].
    If we had started from the first tree, we would only pick from trees [0,1].
    ```

    ```
    Input: fruits = [1,2,3,2,2]
    Output: 4
    Explanation: We can pick from trees [2,3,2,2].
    If we had started from the first tree, we would only pick from trees [1,2].
    ```

    ## Constraints

    - 1 <= fruits.length <= 10^5
    - 0 <= fruits[i] < fruits.length



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import defaultdict

    class Solution:

        def total_fruit(self, fruits: list[int]) -> int:
            raise NotImplementedError('Implement total_fruit')

    practice_exports = {'defaultdict': defaultdict, 'Solution': Solution}
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
