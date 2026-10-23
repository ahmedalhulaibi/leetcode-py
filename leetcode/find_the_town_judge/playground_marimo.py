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
    # 997. Find the Town Judge

    **Easy** · Array, Hash Table, Graph Theory

    In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of these people is secretly the town judge.

    If the town judge exists, then:

    1. The town judge trusts nobody.
    2. Everybody (except for the town judge) trusts the town judge.
    3. There is exactly one person that satisfies properties 1 and 2.

    You are given an array `trust` where `trust[i] = [ai, bi]` representing that the person labeled `ai` trusts the person labeled `bi`. If a trust relationship does not exist in `trust` array, then such a trust relationship does not exist.

    Return *the label of the town judge if the town judge exists and can be identified, or return* `-1` *otherwise*.

    ## Examples

    ```
    Input: n = 2, trust = [[1,2]]
    Output: 2
    ```

    ```
    Input: n = 3, trust = [[1,3],[2,3]]
    Output: 3
    ```

    ```
    Input: n = 3, trust = [[1,3],[2,3],[3,1]]
    Output: -1
    ```

    ## Constraints

    - 1 <= n <= 1000
    - 0 <= trust.length <= 10^4
    - `trust[i].length == 2`
    - All the pairs of `trust` are **unique**.
    - `ai != bi`
    - 1 <= ai, bi <= n



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_judge(self, n: int, trust: list[list[int]]) -> int:
            raise NotImplementedError('Implement find_judge')

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
