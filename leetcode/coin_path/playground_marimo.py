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
    # 656. Coin Path

    **Hard** · Array, Dynamic Programming

    You are given an integer array `coins` **(1-indexed)** of length `n` and an integer `maxJump`. You can jump to any index `i` of the array `coins` if `coins[i] != -1` and you have to pay `coins[i]` when you visit index `i`. In addition to that, if you are currently at index `i`, you can only jump to any index `i + k` where `i + k <= n` and `k` is a value in the range `[1, maxJump]`.

    You are initially positioned at index `1` (`coins[1]` is not -1). You want to find the path that reaches index `n` with the minimum cost.

    Return an integer array of the indices that you will visit in order so that you can reach index `n` with the minimum cost. If there are multiple paths with the same cost, return the lexicographically smallest such path. If it is not possible to reach index `n`, return an empty array.

    ## Examples

    ```
    Input: coins = [1,2,4,-1,2], maxJump = 2
    Output: [1,3,5]
    Explanation: Path 1->3->5 has the cost of coins[1]+coins[3]+coins[5] = 1+4+2 = 7.
    - Path 1->2->5 has the cost of coins[1]+coins[2]+coins[5] = 1+2+2 = 5 which is not the minimum cost.
    ```

    ```
    Input: coins = [1,2,4,-1,2], maxJump = 1
    Output: []
    ```

    ## Constraints

    - 1 <= coins.length <= 1000
    - -1 <= coins[i] <= 100
    - coins[1] != -1
    - 1 <= maxJump <= 100



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def cheapest_jump(self, coins: list[int], max_jump: int) -> list[int]:
            raise NotImplementedError('Implement cheapest_jump')

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
