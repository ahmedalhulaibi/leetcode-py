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
    # 1652. Defuse the Bomb

    **Easy** · Array, Sliding Window

    You have a bomb to defuse, and your time is running out! Your informer will provide you with a **circular** array `code` of length of `n` and a key `k`.

    To decrypt the code, you must replace every number. All the numbers are replaced **simultaneously**.

    - If `k > 0`, replace the `i<sup>th</sup>` number with the sum of the **next** `k` numbers.
    - If `k < 0`, replace the `i<sup>th</sup>` number with the sum of the **previous** `-k` numbers.
    - If `k == 0`, replace the `i<sup>th</sup>` number with `0`.

    As `code` is circular, the next element of `code[n-1]` is `code[0]`, and the previous element of `code[0]` is `code[n-1]`.

    Given the **circular** array `code` and an integer key `k`, return *the decrypted code to defuse the bomb*!

    ## Examples

    ```
    Input: code = [5,7,1,4], k = 3
    Output: [12,10,16,13]
    Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
    ```

    ```
    Input: code = [1,2,3,4], k = 0
    Output: [0,0,0,0]
    Explanation: When k is zero, the numbers are replaced by 0.
    ```

    ```
    Input: code = [2,4,9,3], k = -2
    Output: [12,5,6,13]
    Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.
    ```

    ## Constraints

    - n == code.length
    - 1 <= n <= 100
    - 1 <= code[i] <= 100
    - -(n - 1) <= k <= n - 1

    **Follow up:** Could you solve it in `O(n)` time without scanning the window from scratch for every index?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def decrypt(self, code: list[int], k: int) -> list[int]:
            raise NotImplementedError('Implement decrypt')

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
