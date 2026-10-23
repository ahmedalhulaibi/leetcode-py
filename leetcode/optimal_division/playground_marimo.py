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
    # 553. Optimal Division

    **Medium** · Array, Math, Dynamic Programming

    You are given an integer array `nums`. The adjacent integers in `nums` will perform the float division.

    - For example, for `nums = [2,3,4]`, we will evaluate the expression `"2/3/4"`.

    However, you can add any number of parenthesis at any position to change the priority of operations. You want to add these parentheses such the value of the expression after the evaluation is maximum.

    Return *the corresponding expression that has the maximum value in string format*.

    **Note:** your expression should not contain redundant parenthesis.

    ## Examples

    ```
    Input: nums = [1000,100,10,2]
    Output: "1000/(100/10/2)"
    Explanation: 1000/(100/10/2) = 1000/((100/10)/2) = 200
    However, the bold parenthesis in "1000/((100/10)/2)" are redundant since they do not influence the operation priority.
    So you should return "1000/(100/10/2)".
    Other cases:
    1000/(100/10)/2 = 50
    1000/(100/(10/2)) = 50
    1000/100/10/2 = 0.5
    1000/100/(10/2) = 2
    ```

    ```
    Input: nums = [2,3,4]
    Output: "2/(3/4)"
    Explanation: (2/(3/4)) = 8/3 = 2.667
    It can be shown that after trying all possibilities, we cannot get an expression with evaluation greater than 2.667
    ```

    ## Constraints

    - 1 <= nums.length <= 10
    - 2 <= nums[i] <= 1000
    - There is only one optimal division for the given input.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def optimal_division(self, nums: list[int]) -> str:
            raise NotImplementedError('Implement optimal_division')

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
