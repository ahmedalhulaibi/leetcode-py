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
    # 1052. Grumpy Bookstore Owner

    **Medium** · Array, Sliding Window

    There is a bookstore owner that has a store open for <code>n</code> minutes. You are given an integer array <code>customers</code> of length <code>n</code> where <code>customers[i]</code> is the number of the customers that enter the store at the start of the <code>i<sup>th</sup></code> minute and all those customers leave after the end of that minute.

    During certain minutes, the bookstore owner is grumpy. You are given a binary array <code>grumpy</code> where <code>grumpy[i]</code> is <code>1</code> if the bookstore owner is grumpy during the <code>i<sup>th</sup></code> minute, and is <code>0</code> otherwise.

    When the bookstore owner is grumpy, the customers entering during that minute are not <strong>satisfied</strong>. Otherwise, they are satisfied.

    The bookstore owner knows a secret technique to remain <strong>not grumpy</strong> for <code>minutes</code> consecutive minutes, but this technique can only be used <strong>once</strong>.

    Return the <strong>maximum</strong> number of customers that can be <em>satisfied</em> throughout the day.

    ## Examples

    ```
    Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
    Output: 16
    Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
    ```

    ```
    Input: customers = [1], grumpy = [0], minutes = 1
    Output: 1
    ```

    ## Constraints

    - <code>n == customers.length == grumpy.length</code>
    - <code>1 &lt;= minutes &lt;= n &lt;= 2 * 10<sup>4</sup></code>
    - <code>0 &lt;= customers[i] &lt;= 1000</code>
    - <code>grumpy[i]</code> is either <code>0</code> or <code>1</code>.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_satisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
            raise NotImplementedError('Implement max_satisfied')

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
