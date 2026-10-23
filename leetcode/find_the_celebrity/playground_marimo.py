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
    # 277. Find the Celebrity

    **Medium** · Graph, Two Pointers, Interactive

    Suppose you are at a party with `n` people labeled from `0` to `n - 1` and among them, there may exist one celebrity. The definition of a celebrity is that all the other `n - 1` people know the celebrity, but the celebrity does not know any of them.

    Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

    You are given an integer `n` and a helper function `bool knows(a, b)` that tells you whether `a` knows `b`. Implement a function `int findCelebrity(n)`. There will be exactly one celebrity if they are at the party.

    Return *the celebrity's label if there is a celebrity at the party*. If there is no celebrity, return `-1`.

    **Note** that the `n x n` 2D array `graph` given as input is **not** directly available to you, and instead **only** accessible through the helper function `knows`. `graph[i][j] == 1` represents person `i` knows person `j`, whereas `graph[i][j] == 0` represents person `i` does not know person `j`.

    **Follow up:** If the maximum number of allowed calls to the API `knows` is `3 * n`, could you find a solution without exceeding the maximum number of calls?

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0277.Find%20the%20Celebrity/images/g1.jpg)

    ```
    Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
    Output: 1
    Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0277.Find%20the%20Celebrity/images/g2.jpg)

    ```
    Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
    Output: -1
    Explanation: There is no celebrity.
    ```

    ## Constraints

    - `n == graph.length == graph[i].length`
    - `2 <= n <= 100`
    - `graph[i][j]` is `0` or `1`.
    - `graph[i][i] == 1`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from typing import ClassVar

    class Solution:
        graph: ClassVar[list[list[int]]] = []

        def knows(self, a: int, b: int) -> bool:
            raise NotImplementedError('Implement knows')

        def find_celebrity(self, n: int) -> int:
            raise NotImplementedError('Implement find_celebrity')

    practice_exports = {'ClassVar': ClassVar, 'Solution': Solution}
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
