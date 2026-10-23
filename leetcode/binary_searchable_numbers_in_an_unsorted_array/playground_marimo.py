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
    # 1966. Binary Searchable Numbers in an Unsorted Array

    **Medium** · Array, Binary Search, Stack, Monotonic Stack

    <p>Consider a function that implements an algorithm <strong>similar</strong> to <a href="https://leetcode.com/explore/learn/card/binary-search/" target="_blank">Binary Search</a>. The function has two input parameters: <code>sequence</code> is a sequence of integers, and <code>target</code> is an integer value. The purpose of the function is to find if the <code>target</code> exists in the <code>sequence</code>.</p>

    <p>The pseudocode of the function is as follows:</p>

    <pre>
    func(sequence, target)
      while sequence is not empty
        <strong>randomly</strong> choose an element from sequence as the pivot
        if pivot = target, return <strong>true</strong>
        else if pivot &lt; target, remove pivot and all elements to its left from the sequence
        else, remove pivot and all elements to its right from the sequence
      end while
      return <strong>false</strong>
    </pre>

    <p>When the <code>sequence</code> is sorted, the function works correctly for <strong>all</strong> values. When the <code>sequence</code> is not sorted, the function does not work for all values, but may still work for <strong>some</strong> values.</p>

    <p>Given an integer array <code>nums</code>, representing the <code>sequence</code>, that contains <strong>unique</strong> numbers and <strong>may or may not be sorted</strong>, return <em>the number of values that are <strong>guaranteed</strong> to be found using the function, for <strong>every possible</strong> pivot selection</em>.</p>

    ## Examples

    ```
    Input: nums = [7]
    Output: 1
    Explanation:
    Searching for value 7 is guaranteed to be found.
    Since the sequence has only one element, 7 will be chosen as the pivot. Because the pivot equals the target, the function will return true.
    ```

    ```
    Input: nums = [-1,5,2]
    Output: 1
    Explanation:
    Searching for value -1 is guaranteed to be found.
    If -1 was chosen as the pivot, the function would return true.
    If 5 was chosen as the pivot, 5 and 2 would be removed. In the next loop, the sequence would have only -1 and the function would return true.
    If 2 was chosen as the pivot, 2 would be removed. In the next loop, the sequence would have -1 and 5. No matter which number was chosen as the next pivot, the function would find -1 and return true.

    Searching for value 5 is NOT guaranteed to be found.
    If 2 was chosen as the pivot, -1, 5 and 2 would be removed. The sequence would be empty and the function would return false.

    Searching for value 2 is NOT guaranteed to be found.
    If 5 was chosen as the pivot, 5 and 2 would be removed. In the next loop, the sequence would have only -1 and the function would return false.

    Because only -1 is guaranteed to be found, you should return 1.
    ```

    ## Constraints

    - 1 &lt;= nums.length &lt;= 10<sup>5</sup>
    - -10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup>
    - All the values of <code>nums</code> are <strong>unique</strong>.

    <p><strong>Follow-up:</strong> If <code>nums</code> has <strong>duplicates</strong>, would you modify your algorithm? If so, how?</p>

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def binary_searchable_numbers(self, nums: list[int]) -> int:
            raise NotImplementedError('Implement binary_searchable_numbers')

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
