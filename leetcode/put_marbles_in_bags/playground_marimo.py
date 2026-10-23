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
    # 2551. Put Marbles in Bags

    **Hard** · Array, Greedy, Sorting, Heap (Priority Queue)

    You have `k` bags. You are given a **0-indexed** integer array `weights` where `weights[i]` is the weight of the `i`th marble. You are also given the integer `k`.

    Divide the marbles into the `k` bags according to the following rules:

    - No bag is empty.
    - If the `i`th marble and `j`th marble are in a bag, then all marbles with an index between the `i`th and `j`th indices should also be in that same bag.
    - If a bag consists of all the marbles with an index from `i` to `j` inclusively, then the cost of the bag is `weights[i] + weights[j]`.

    The **score** after distributing the marbles is the sum of the costs of all the `k` bags.

    Return the difference between the maximum and minimum scores among marble distributions.

    ## Examples

    ```
    Input: weights = [1,3,5,1], k = 2
    Output: 4
    Explanation:
    The distribution [1],[3,5,1] results in the minimal score of (1+1) + (3+1) = 6.
    The distribution [1,3],[5,1], results in the maximal score of (1+3) + (5+1) = 10.
    Thus, we return their difference 10 - 6 = 4.
    ```

    ```
    Input: weights = [1, 3], k = 2
    Output: 0
    Explanation: The only distribution possible is [1],[3].
    Since both the maximal and minimal score are the same, we return 0.
    ```

    ## Constraints

    - `1 <= k <= weights.length <= 10^5`
    - `1 <= weights[i] <= 10^9`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def put_marbles(self, weights: list[int], k: int) -> int:
            raise NotImplementedError('Implement put_marbles')

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
