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
    # 3199. Count Triplets with Even XOR Set Bits I

    **Easy** · Array, Bit Manipulation

    Given three integer arrays `a`, `b`, and `c`, return the number of triplets `(a[i], b[j], c[k])`, such that the bitwise `XOR` of the elements of each triplet has an **even** number of set bits.

    ## Examples

    ```
    Input: a = [1], b = [2], c = [3]
    Output: 1
    Explanation:
    The only triplet is (a[0], b[0], c[0]) and their XOR is: 1 XOR 2 XOR 3 = 00_2.
    ```

    ```
    Input: a = [1,1], b = [2,3], c = [1,5]
    Output: 4
    Explanation:
    Consider these four triplets:
    - (a[0], b[1], c[0]): 1 XOR 3 XOR 1 = 011_2
    - (a[1], b[1], c[0]): 1 XOR 3 XOR 1 = 011_2
    - (a[0], b[0], c[1]): 1 XOR 2 XOR 5 = 110_2
    - (a[1], b[0], c[1]): 1 XOR 2 XOR 5 = 110_2
    ```

    ## Constraints

    - 1 <= a.length, b.length, c.length <= 100
    - 0 <= a[i], b[i], c[i] <= 100



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def triplet_count(self, a: list[int], b: list[int], c: list[int]) -> int:
            raise NotImplementedError('Implement triplet_count')

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
