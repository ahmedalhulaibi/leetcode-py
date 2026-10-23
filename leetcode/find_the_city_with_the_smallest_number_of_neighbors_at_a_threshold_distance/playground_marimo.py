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
    # 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

    **Medium** · Dynamic Programming, Graph Theory, Shortest Path, Dijkstra's Algorithm, Bellman-Ford Algorithm, Floyd-Warshall Algorithm

    There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

    Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

    Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2024/08/23/problem1334example0.png)

    ```
    Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
    Output: 3
    Explanation: The figure above describes the graph.
    The neighboring cities at a distanceThreshold = 4 for each city are:
    City 0 -> [City 1, City 2]
    City 1 -> [City 0, City 2, City 3]
    City 2 -> [City 0, City 1, City 3]
    City 3 -> [City 1, City 2]
    Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2024/08/23/problem1334example1.png)

    ```
    Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
    Output: 0
    Explanation: The figure above describes the graph.
    The neighboring cities at a distanceThreshold = 2 for each city are:
    City 0 -> [City 1]
    City 1 -> [City 0, City 4]
    City 2 -> [City 3, City 4]
    City 3 -> [City 2, City 4]
    City 4 -> [City 1, City 2, City 3]
    The city 0 has 1 neighboring city at a distanceThreshold = 2.
    ```

    ## Constraints

    - 2 <= n <= 100
    - 1 <= edges.length <= n * (n - 1) / 2
    - edges[i].length == 3
    - 0 <= fromi < toi < n
    - 1 <= weighti, distanceThreshold <= 10^4
    - All pairs (fromi, toi) are distinct.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_the_city(self, n: int, edges: list[list[int]], distance_threshold: int) -> int:
            raise NotImplementedError('Implement find_the_city')

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
