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
    # 2492. Minimum Score of a Path Between Two Cities

    **Medium** · Depth-First Search, Breadth-First Search, Union-Find, Graph Theory

    You are given a positive integer `n` representing `n` cities numbered from `1` to `n`. You are also given a **2D** array `roads` where `roads[i] = [ai, bi, distancei]` indicates that there is a bidirectional road between cities `ai` and `bi` with a distance equal to `distancei`. The cities graph is not necessarily connected.

    The score of a path between two cities is defined as the minimum distance of a road in this path.

    Return *the minimum possible score of a path between cities* `1` *and* `n`.

    **Note:**

    - A path is a sequence of roads between two cities.
    - It is allowed for a path to contain the same road multiple times, and you can visit cities `1` and `n` multiple times along the path.
    - The test cases are generated such that there is at least one path between `1` and `n`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/10/12/graph11.png)

    ```
    Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
    Output: 5
    Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
    It can be shown that no other path has less score.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2022/10/12/graph22.png)

    ```
    Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
    Output: 2
    Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.
    ```

    ## Constraints

    - 2 <= n <= 10^5
    - 1 <= roads.length <= 10^5
    - roads[i].length == 3
    - 1 <= ai, bi <= n
    - ai != bi
    - 1 <= distancei <= 10^4
    - There are no repeated edges.
    - There is at least one path between 1 and n.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_score(self, n: int, roads: list[list[int]]) -> int:
            raise NotImplementedError('Implement min_score')

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
