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
    # 2226. Maximum Candies Allocated to K Children

    **Medium** · Array, Binary Search

    You are given a <strong>0-indexed</strong> integer array <code>candies</code>. Each element in the array denotes a pile of candies of size <code>candies[i]</code>. You can divide each pile into any number of <strong>sub piles</strong>, but you <strong>cannot</strong> merge two piles together.

    You are also given an integer <code>k</code>. You should allocate piles of candies to <code>k</code> children such that each child gets the <strong>same</strong> number of candies. Each child can be allocated candies from <strong>only one</strong> pile of candies and some piles of candies may go unused.

    Return <em>the <strong>maximum number of candies</strong> each child can get.</em>

    ## Examples

    ```
    Input: candies = [5,8,6], k = 3
    Output: 5
    Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.
    ```

    ```
    Input: candies = [2,5], k = 11
    Output: 0
    Explanation: There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.
    ```

    ## Constraints

    - 1 <= candies.length <= 10<sup>5</sup>
    - 1 <= candies[i] <= 10<sup>7</sup>
    - 1 <= k <= 10<sup>12</sup>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def maximum_candies(self, candies: list[int], k: int) -> int:
            raise NotImplementedError('Implement maximum_candies')

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
