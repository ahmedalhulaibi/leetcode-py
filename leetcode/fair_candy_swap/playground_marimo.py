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
    # 888. Fair Candy Swap

    **Easy** · Array, Hash Table, Binary Search, Sorting

    Alice and Bob have a different total number of candies. You are given two integer arrays `aliceSizes` and `bobSizes` where `aliceSizes[i]` is the number of candies of the `i`th box of candy that Alice has and `bobSizes[j]` is the number of candies of the `j`th box of candy that Bob has.

    Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.

    Return an integer array `answer` where `answer[0]` is the number of candies in the box that Alice must exchange, and `answer[1]` is the number of candies in the box that Bob must exchange. If there are multiple answers, you may return any one of them. It is guaranteed that at least one answer exists.

    ## Examples

    ```
    Input: aliceSizes = [1,1], bobSizes = [2,2]
    Output: [1,2]
    ```

    ```
    Input: aliceSizes = [1,2], bobSizes = [2,3]
    Output: [1,2]
    ```

    ```
    Input: aliceSizes = [2], bobSizes = [1,3]
    Output: [2,3]
    ```

    ## Constraints

    - `1 <= aliceSizes.length, bobSizes.length <= 10^4`
    - `1 <= aliceSizes[i], bobSizes[j] <= 10^5`
    - Alice and Bob have a different total number of candies.
    - There will be at least one valid answer for the given input.

    **Follow up:** Can you solve it in `O(n)` time complexity?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def fair_candy_swap(self, alice_sizes: list[int], bob_sizes: list[int]) -> list[int]:
            raise NotImplementedError('Implement fair_candy_swap')

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
