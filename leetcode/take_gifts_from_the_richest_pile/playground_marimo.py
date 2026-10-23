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
    # 2558. Take Gifts From the Richest Pile

    **Easy** · Array, Heap (Priority Queue), Simulation

    You are given an integer array `gifts` denoting the number of gifts in various piles. Every second, you do the following:

    - Choose the pile with the maximum number of gifts.
    - If there is more than one pile with the maximum number of gifts, choose any.
    - Reduce the number of gifts in the pile to the floor of the square root of the original number of gifts in the pile.

    Return *the number of gifts remaining after* `k` *seconds.*

    ## Examples

    ```
    Input: gifts = [25,64,9,4,100], k = 4
    Output: 29
    Explanation:
    The gifts are taken in the following way:
    - In the first second, the last pile is chosen and 10 gifts are left behind.
    - Then the second pile is chosen and 8 gifts are left behind.
    - After that the first pile is chosen and 5 gifts are left behind.
    - Finally, the last pile is chosen again and 3 gifts are left behind.
    The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.
    ```

    ```
    Input: gifts = [1,1,1,1], k = 4
    Output: 4
    Explanation:
    In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile.
    That is, you can't take any pile with you.
    So, the total gifts remaining are 4.
    ```

    ## Constraints

    - 1 <= gifts.length <= 10<sup>3</sup>
    - 1 <= gifts[i] <= 10<sup>9</sup>
    - 1 <= k <= 10<sup>3</sup>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def pick_gifts(self, gifts: list[int], k: int) -> int:
            raise NotImplementedError('Implement pick_gifts')

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
