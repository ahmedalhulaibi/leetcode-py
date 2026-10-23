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
    # 1231. Divide Chocolate

    **Hard** · Array, Binary Search

    You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array `sweetness`.

    You want to share the chocolate with your `k` friends so you start cutting the chocolate bar into `k + 1` pieces using `k` cuts, each piece consists of some <strong>consecutive</strong> chunks.

    Being generous, you will eat the piece with the <strong>minimum total sweetness</strong> and give the other pieces to your friends.

    Find the <strong>maximum total sweetness</strong> of the piece you can get by cutting the chocolate bar optimally.

    ## Examples

    ```
    Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
    Output: 6
    Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
    ```

    ```
    Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
    Output: 1
    Explanation: There is only one way to cut the bar into 9 pieces.
    ```

    ```
    Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
    Output: 5
    Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
    ```

    ## Constraints

    - 0 <= k < sweetness.length <= 10<sup>4</sup>
    - 1 <= sweetness[i] <= 10<sup>5</sup>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def maximize_sweetness(self, sweetness: list[int], k: int) -> int:
            raise NotImplementedError('Implement maximize_sweetness')

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
