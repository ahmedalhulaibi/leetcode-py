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
    # 952. Largest Component Size by Common Factor

    **Hard** · Array, Hash Table, Math, Union-Find, Number Theory, Prime Factorization

    Given an integer array of unique positive integers `nums`. Consider the following graph:

    - There are `nums.length` nodes, labeled `nums[0]` to `nums[nums.length - 1]`,
    - There is an undirected edge between `nums[i]` and `nums[j]` if `nums[i]` and `nums[j]` share a common factor greater than `1`.

    Return the size of the largest connected component in the graph.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2018/12/01/ex1.png)

    ```
    Input: nums = [4,6,15,35]
    Output: 4
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2018/12/01/ex2.png)

    ```
    Input: nums = [20,50,9,63]
    Output: 2
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2018/12/01/ex3.png)

    ```
    Input: nums = [2,3,6,7,4,12,21,39]
    Output: 8
    ```

    ## Constraints

    - 1 <= nums.length <= 2 * 10^4
    - 1 <= nums[i] <= 10^5
    - All the values of nums are unique.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def largest_component_size(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement largest_component_size')

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
