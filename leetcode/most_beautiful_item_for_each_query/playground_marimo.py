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
    # 2070. Most Beautiful Item for Each Query

    **Medium** · Array, Binary Search, Sorting

    You are given a 2D integer array items where items[i] = [price<sub>i</sub>, beauty<sub>i</sub>] denotes the <b>price</b> and <b>beauty</b> of an item respectively.

    You are also given a <b>0-indexed</b> integer array queries. For each queries[j], you want to determine the <b>maximum beauty</b> of an item whose <b>price</b> is <b>less than or equal</b> to queries[j]. If no such item exists, then the answer to this query is 0.

    Return an array answer of the same length as queries where answer[j] is the answer to the j<sup>th</sup> query.

    ## Examples

    ```
    Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
    Output: [2,4,5,5,6,6]
    Explanation:
    - For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
    - For queries[1]=2, the items which can be considered are [1,2] and [2,4]. The maximum beauty among them is 4.
    - For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5]. The maximum beauty among them is 5.
    - For queries[4]=5 and queries[5]=6, all items can be considered. Hence, the answer for them is the maximum beauty of all items, i.e., 6.
    ```

    ```
    Input: items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
    Output: [4]
    Explanation: The price of every item is equal to 1, so we choose the item with the maximum beauty 4. Note that multiple items can have the same price and/or beauty.
    ```

    ```
    Input: items = [[10,1000]], queries = [5]
    Output: [0]
    Explanation: No item has a price less than or equal to 5, so no item can be chosen. Hence, the answer to the query is 0.
    ```

    ## Constraints

    - 1 <= items.length, queries.length <= 10^5
    - items[i].length == 2
    - 1 <= price_i, beauty_i, queries[j] <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def maximum_beauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
            raise NotImplementedError('Implement maximum_beauty')

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
