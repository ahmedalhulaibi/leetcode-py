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
    # 1000. Minimum Cost to Merge Stones

    **Hard** · Array, Dynamic Programming, Prefix Sum

    There are `n` piles of stones arranged in a row. The `i^th` pile has `stones[i]` stones.

    A move consists of merging exactly `k` **consecutive** piles into one pile, and the cost of this move is equal to the total number of stones in these `k` piles.

    Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return `-1`.

    ## Examples

    ```
    Input: stones = [3,2,4,1], k = 2
    Output: 20
    ```
    **Explanation:** We start with [3, 2, 4, 1].
    We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
    We merge [4, 1] for a cost of 5, and we are left with [5, 5].
    We merge [5, 5] for a cost of 10, and we are left with [10].
    The total cost was 20, and this is the minimum possible.

    ```
    Input: stones = [3,2,4,1], k = 3
    Output: -1
    ```
    **Explanation:** After any merge operation, there are 2 piles left, and we can't merge anymore. So the task is impossible.

    ```
    Input: stones = [3,5,1,2,6], k = 3
    Output: 25
    ```
    **Explanation:** We start with [3, 5, 1, 2, 6].
    We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
    We merge [3, 8, 6] for a cost of 17, and we are left with [17].
    The total cost was 25, and this is the minimum possible.

    ## Constraints

    - `n == stones.length`
    - `1 <= n <= 30`
    - `1 <= stones[i] <= 100`
    - `2 <= k <= 30`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def merge_stones(self, stones: list[int], k: int) -> int:
            raise NotImplementedError('Implement merge_stones')

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
