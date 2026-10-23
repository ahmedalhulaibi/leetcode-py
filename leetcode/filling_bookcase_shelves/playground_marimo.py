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
    # 1105. Filling Bookcase Shelves

    **Medium** · Array, Dynamic Programming

    You are given an array <code>books</code> where <code>books[i] = [thickness<sub>i</sub>, height<sub>i</sub>]</code> indicates the thickness and height of the <code>i<sup>th</sup></code> book. You are also given an integer <code>shelfWidth</code>.

    We want to place these books in order onto bookcase shelves that have a total width <code>shelfWidth</code>.

    We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to <code>shelfWidth</code>, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

    Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

    For example, if we have an ordered list of <code>5</code> books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

    Return <em>the minimum possible height that the total bookshelf can be after placing shelves in this manner</em>.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/06/24/shelves.png)

    ```
    Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
    Output: 6
    Explanation: The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6. Notice that book number 2 does not have to be on the first shelf.
    ```

    ```
    Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
    Output: 4
    ```

    ## Constraints

    - <code>1 &lt;= books.length &lt;= 1000</code>
    - <code>1 &lt;= thickness<sub>i</sub> &lt;= shelfWidth &lt;= 1000</code>
    - <code>1 &lt;= height<sub>i</sub> &lt;= 1000</code>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_height_shelves(self, books: list[list[int]], shelf_width: int) -> int:
            raise NotImplementedError('Implement min_height_shelves')

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
