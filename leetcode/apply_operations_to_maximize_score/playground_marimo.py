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
    mo.md(r"""
    # 2818. Apply Operations to Maximize Score

    **Hard** · Array, Math, Stack, Greedy, Sorting, Monotonic Stack, Number Theory

    <p>You are given an array <code>nums</code> of <code>n</code> positive integers and an integer <code>k</code>.</p>

    <p>Initially, you start with a score of <code>1</code>. You have to maximize your score by applying the following operation at most <code>k</code> times:</p>

    <ul>
        <li>Choose any <strong>non-empty</strong> subarray <code>nums[l, ..., r]</code> that you haven't chosen previously.</li>
        <li>Choose an element <code>x</code> of <code>nums[l, ..., r]</code> with the highest <strong>prime score</strong>. If multiple such elements exist, choose the one with the smallest index.</li>
        <li>Multiply your score by <code>x</code>.</li>
    </ul>

    <p>Here, <code>nums[l, ..., r]</code> denotes the subarray of <code>nums</code> starting at index <code>l</code> and ending at the index <code>r</code>, both ends being inclusive.</p>

    <p>The <strong>prime score</strong> of an integer <code>x</code> is equal to the number of distinct prime factors of <code>x</code>. For example, the prime score of <code>300</code> is <code>3</code> since <code>300 = 2 * 2 * 3 * 5 * 5</code>.</p>

    <p>Return <em>the <strong>maximum possible score</strong> after applying at most </em><code>k</code><em> operations</em>.</p>

    <p>Since the answer may be large, return it modulo <code>10<sup>9 </sup>+ 7</code>.</p>

    ## Examples

    ```
    Input: nums = [8,3,9,3,8], k = 2
    Output: 81
    Explanation: To get a score of 81, we can apply the following operations:
    - Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
    - Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
    It can be proven that 81 is the highest score one can obtain.
    ```

    ```
    Input: nums = [19,12,14,6,10,18], k = 3
    Output: 4788
    Explanation: To get a score of 4788, we can apply the following operations:
    - Choose subarray nums[0, ..., 0]. nums[0] is the only element in this subarray. Hence, we multiply the score by nums[0]. The score becomes 1 * 19 = 19.
    - Choose subarray nums[5, ..., 5]. nums[5] is the only element in this subarray. Hence, we multiply the score by nums[5]. The score becomes 19 * 18 = 342.
    - Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 2, but nums[2] has the smaller index. Hence, we multipy the score by nums[2]. The score becomes 342 * 14 = 4788.
    It can be proven that 4788 is the highest score one can obtain.
    ```

    ## Constraints

    - 1 <= nums.length == n <= 10^5
    - 1 <= nums[i] <= 10^5
    - 1 <= k <= min(n * (n + 1) / 2, 10^9)



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def maximum_score(self, nums: list[int], k: int) -> int:
            raise NotImplementedError('Implement maximum_score')

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
