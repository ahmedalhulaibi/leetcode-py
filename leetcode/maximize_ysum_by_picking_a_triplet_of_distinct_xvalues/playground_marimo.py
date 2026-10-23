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
    mo.md(r"""
    # 3572. Maximize Y-Sum by Picking a Triplet of Distinct X-Values

    **Medium** · Array, Hash Table, Greedy, Sorting, Heap (Priority Queue)

    You are given two integer arrays <code>x</code> and <code>y</code>, each of length <code>n</code>. You must choose three <strong>distinct</strong> indices <code>i</code>, <code>j</code>, and <code>k</code> such that:

    <ul>
        <li><code>x[i] != x[j]</code></li>
        <li><code>x[j] != x[k]</code></li>
        <li><code>x[k] != x[i]</code></li>
    </ul>

    Your goal is to <strong>maximize</strong> the value of <code>y[i] + y[j] + y[k]</code> under these conditions. Return the <strong>maximum</strong> possible sum that can be obtained by choosing such a triplet of indices.

    If no such triplet exists, return -1.

    ## Examples

    ```
    Input: x = [1,2,1,3,2], y = [5,3,4,6,2]
    Output: 14
    Explanation: Choose i = 0 (x[i] = 1, y[i] = 5), j = 1 (x[j] = 2, y[j] = 3), k = 3 (x[k] = 3, y[k] = 6). All three values chosen from x are distinct. 5 + 3 + 6 = 14 is the maximum we can obtain.
    ```

    ```
    Input: x = [1,2,1,2], y = [4,5,6,7]
    Output: -1
    Explanation: There are only two distinct values in x. Hence, the output is -1.
    ```

    ## Constraints

    - n == x.length == y.length
    - 3 <= n <= 10^5
    - 1 <= x[i], y[i] <= 10^6



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_sum_distinct_triplet(self, x: list[int], y: list[int]) -> int:
            raise NotImplementedError('Implement max_sum_distinct_triplet')

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
