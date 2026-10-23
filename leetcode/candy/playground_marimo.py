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
    # 135. Candy

    **Hard** · Array, Greedy

    There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

    You are giving candies to these children subjected to the following requirements:

    - Each child must have at least one candy.
    - Children with a higher rating get more candies than their neighbors.

    Return *the minimum number of candies you need to have to distribute the candies to the children*.

    ## Examples

    ```
    Input: ratings = [1,0,2]
    Output: 5
    ```
    **Explanation:** You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

    ```
    Input: ratings = [1,2,2]
    Output: 4
    ```
    **Explanation:** You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
    The third child gets 1 candy because it satisfies the above two conditions.

    ## Constraints

    - n == ratings.length
    - 1 <= n <= 2 * 10^4
    - 0 <= ratings[i] <= 2 * 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def candy(self, ratings: list[int]) -> int:
            raise NotImplementedError('Implement candy')

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
