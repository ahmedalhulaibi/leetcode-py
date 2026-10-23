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
    # 2251. Number of Flowers in Full Bloom

    **Hard** · Array, Hash Table, Binary Search, Sorting, Prefix Sum, Ordered Set

    You are given a **0-indexed** 2D integer array `flowers`, where `flowers[i] = [starti, endi]` means the `ith` flower will be in **full bloom** from `starti` to `endi` (**inclusive**). You are also given a **0-indexed** integer array `people` of size `n`, where `people[i]` is the time that the `ith` person will arrive to see the flowers.

    Return an integer array `answer` of size `n`, where `answer[i]` is the **number** of flowers that are in full bloom when the `ith` person arrives.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/03/02/ex1new.jpg)

    ```
    Input: flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
    Output: [1,2,2,2]
    ```
    **Explanation:** The figure above shows the times when the flowers are in full bloom and when the people arrive. For each person, we return the number of flowers in full bloom during their arrival.

    ![Example 2](https://assets.leetcode.com/uploads/2022/03/02/ex2new.jpg)

    ```
    Input: flowers = [[1,10],[3,3]], people = [3,3,2]
    Output: [2,2,1]
    ```
    **Explanation:** The figure above shows the times when the flowers are in full bloom and when the people arrive. For each person, we return the number of flowers in full bloom during their arrival.

    ## Constraints

    - `1 <= flowers.length <= 5 * 10^4`
    - `flowers[i].length == 2`
    - `1 <= starti <= endi <= 10^9`
    - `1 <= people.length <= 5 * 10^4`
    - `1 <= people[i] <= 10^9`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def full_bloom_flowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
            raise NotImplementedError('Implement full_bloom_flowers')

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
