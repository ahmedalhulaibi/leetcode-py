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
    # 1196. How Many Apples Can You Put into the Basket

    **Easy** · Array, Greedy, Sorting

    You have some apples and a basket that can carry up to `5000` units of weight.

    Given an integer array `weight` where `weight[i]` is the weight of the `i-th` apple, return the maximum number of apples you can put in the basket.

    ## Examples

    ```
    Input: weight = [100,200,150,1000]
    Output: 4
    Explanation: All 4 apples can be carried by the basket since their sum of weights is 1450.
    ```

    ```
    Input: weight = [900,950,800,1000,700,800]
    Output: 5
    Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any 5 of them.
    ```

    ## Constraints

    - `1 <= weight.length <= 10^3`
    - `1 <= weight[i] <= 10^3`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_number_of_apples(self, weight: list[int]) -> int:
            raise NotImplementedError('Implement max_number_of_apples')

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
