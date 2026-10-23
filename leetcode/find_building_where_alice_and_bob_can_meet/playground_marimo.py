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
    # 2940. Find Building Where Alice and Bob Can Meet

    **Hard** · Array, Binary Search, Stack, Binary Indexed Tree, Segment Tree, Heap (Priority Queue), Monotonic Stack

    You are given a **0-indexed** array `heights` of positive integers, where `heights[i]` represents the height of the `i`th building.

    If a person is in building `i`, they can move to any other building `j` if and only if `i < j` and `heights[i] < heights[j]`.

    You are also given another array `queries` where `queries[i] = [a_i, b_i]`. On the `i`th query, Alice is in building `a_i` while Bob is in building `b_i`.

    Return *an array* `ans` where `ans[i]` is **the index of the leftmost building** where Alice and Bob can meet on the `i`th query. If Alice and Bob cannot move to a common building on query `i`, set `ans[i]` to `-1`.

    ## Examples

    ```
    Input: heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
    Output: [2,5,-1,5,2]
    Explanation: In the first query, Alice and Bob can move to building 2 since heights[0] < heights[2] and heights[1] < heights[2].
    In the second query, Alice and Bob can move to building 5 since heights[0] < heights[5] and heights[3] < heights[5].
    In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
    In the fourth query, Alice and Bob can move to building 5 since heights[3] < heights[5] and heights[4] < heights[5].
    In the fifth query, Alice and Bob are already in the same building.
    For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
    For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.
    ```

    ```
    Input: heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
    Output: [7,6,-1,4,6]
    Explanation: In the first query, Alice can directly move to Bob's building since heights[0] < heights[7].
    In the second query, Alice and Bob can move to building 6 since heights[3] < heights[6] and heights[5] < heights[6].
    In the third query, Alice cannot meet Bob since Bob cannot move to any other building.
    In the fourth query, Alice and Bob can move to building 4 since heights[3] < heights[4] and heights[0] < heights[4].
    In the fifth query, Alice can directly move to Bob's building since heights[1] < heights[6].
    For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
    For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.
    ```

    ## Constraints

    - 1 <= heights.length <= 5 * 10^4
    - 1 <= heights[i] <= 10^9
    - 1 <= queries.length <= 5 * 10^4
    - queries[i] = [a_i, b_i]
    - 0 <= a_i, b_i <= heights.length - 1



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def leftmost_building_queries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
            raise NotImplementedError('Implement leftmost_building_queries')

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
