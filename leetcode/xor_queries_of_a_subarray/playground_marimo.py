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
    # 1310. XOR Queries of a Subarray

    **Medium** · Array, Bit Manipulation, Prefix Sum

    You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

    For each query i, compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti]).

    Return an array answer where answer[i] is the answer to the ith query.

    ## Examples

    ```
    Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
    Output: [2,7,14,8]
    Explanation:
    The binary representation of the elements in the array are:
    1 = 0001
    3 = 0011
    4 = 0100
    8 = 1000
    The XOR values for queries are:
    [0,1] = 1 xor 3 = 2
    [1,2] = 3 xor 4 = 7
    [0,3] = 1 xor 3 xor 4 xor 8 = 14
    [3,3] = 8
    ```

    ```
    Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
    Output: [8,0,4,4]
    ```

    ## Constraints

    - 1 <= arr.length, queries.length <= 3 * 10^4
    - 1 <= arr[i] <= 10^9
    - queries[i].length == 2
    - 0 <= lefti <= righti < arr.length



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def xor_queries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
            raise NotImplementedError('Implement xor_queries')

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
