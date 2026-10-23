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
    # 339. Nested List Weight Sum

    **Medium** · Depth-First Search, Breadth-First Search

    You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists.

    The **depth** of an integer is the number of lists that it is inside of. For example, the nested list `[1,[2,2],[[3],2],1]` has each integer's value set to its **depth**.

    Return *the sum of each integer in* `nestedList` *multiplied by its **depth***.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0339.Nested%20List%20Weight%20Sum/images/nestedlistweightsumex1.png)

    ```
    Input: nestedList = [[1,1],2,[1,1]]
    Output: 10
    Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0339.Nested%20List%20Weight%20Sum/images/nestedlistweightsumex2.png)

    ```
    Input: nestedList = [1,[4,[6]]]
    Output: 27
    Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
    ```

    ```
    Input: nestedList = [0]
    Output: 0
    ```

    ## Constraints

    - `1 <= nestedList.length <= 50`
    - The values of the integers in the nested list is in the range `[-100, 100]`.
    - The maximum **depth** of any integer is less than or equal to `50`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from typing import Any

    class Solution:

        def depth_sum(self, nested_list: list[Any]) -> int:
            raise NotImplementedError('Implement depth_sum')

    practice_exports = {'Any': Any, 'Solution': Solution}
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
