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
    # 3243. Shortest Distance After Road Addition Queries I

    **Medium** · Array, Breadth-First Search, Graph Theory

    You are given an integer <code>n</code> and a 2D integer array <code>queries</code>.

    There are <code>n</code> cities numbered from <code>0</code> to <code>n - 1</code>. Initially, there is a <strong>unidirectional</strong> road from city <code>i</code> to city <code>i + 1</code> for all <code>0 &lt;= i &lt; n - 1</code>.

    <code>queries[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> represents the addition of a new <strong>unidirectional</strong> road from city <code>u<sub>i</sub></code> to city <code>v<sub>i</sub></code>. After each query, you need to find the <strong>length</strong> of the <strong>shortest path</strong> from city <code>0</code> to city <code>n - 1</code>.

    Return an array <code>answer</code> where for each <code>i</code> in the range <code>[0, queries.length - 1]</code>, <code>answer[i]</code> is the length of the shortest path from city <code>0</code> to city <code>n - 1</code> after processing the <strong>first</strong> <code>i + 1</code> queries.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2024/06/28/image8.jpg)

    ```
    Input: n = 5, queries = [[2,4],[0,2],[0,4]]
    Output: [3,2,1]
    Explanation:

    After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.
    ```

    ![Example 1](https://assets.leetcode.com/uploads/2024/06/28/image9.jpg)

    After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.

    ![Example 1](https://assets.leetcode.com/uploads/2024/06/28/image10.jpg)

    After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

    ![Example 2](https://assets.leetcode.com/uploads/2024/06/28/image11.jpg)

    ```
    Input: n = 4, queries = [[0,3],[0,2]]
    Output: [1,1]
    Explanation:

    After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2024/06/28/image12.jpg)

    After the addition of the road from 0 to 2, the length of the shortest path remains 1.

    ## Constraints

    - <code>3 &lt;= n &lt;= 500</code>
    - <code>1 &lt;= queries.length &lt;= 500</code>
    - <code>queries[i].length == 2</code>
    - <code>0 &lt;= queries[i][0] &lt; queries[i][1] &lt; n</code>
    - <code>1 &lt; queries[i][1] - queries[i][0]</code>
    - There are no repeated roads among the queries.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import deque

    class Solution:

        def shortest_distance_after_queries(self, n: int, queries: list[list[int]]) -> list[int]:
            raise NotImplementedError('Implement shortest_distance_after_queries')

    practice_exports = {'deque': deque, 'Solution': Solution}
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
