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
    # 97. Interleaving String

    **Medium** · String, Dynamic Programming

    Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an **interleaving** of `s1` and `s2`.

    An interleaving of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that:

    - s = s1 + s2 + ... + sn
    - t = t1 + t2 + ... + tm
    - |n - m| <= 1
    - The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

    **Note:** `a + b` is the concatenation of strings `a` and `b`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg)

    ```
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true
    Explanation: One way to obtain s3 is:
    Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
    Interleaving the two splits, we get "aadbbcbcac".
    ```

    ```
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: false
    Explanation: Notice how it is hard to find a viable interleaving because s3 must preserve the character order of s1 and s2.
    ```

    ```
    Input: s1 = "\", s2 = "\", s3 = "\"
    Output: true
    ```

    ## Constraints

    - 0 <= s1.length, s2.length <= 100
    - 0 <= s3.length <= 200
    - s1, s2, and s3 consist of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_interleave(self, s1: str, s2: str, s3: str) -> bool:
            raise NotImplementedError('Implement is_interleave')

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
