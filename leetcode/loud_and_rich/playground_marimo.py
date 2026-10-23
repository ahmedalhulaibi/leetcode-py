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
    # 851. Loud and Rich

    **Medium** · Array, Depth-First Search, Graph Theory, Topological Sort, Directed Acyclic Graph

    There is a group of `n` people labeled from `0` to `n - 1` where each person has a different amount of money and a different level of quietness.

    You are given an array `richer` where `richer[i] = [ai, bi]` indicates that `ai` has more money than `bi` and an integer array `quiet` where `quiet[i]` is the quietness of the `ith` person. All the given data in richer are **logically correct** (i.e., the data will not lead you to a situation where `x` is richer than `y` and `y` is richer than `x` at the same time).

    Return *an integer array* `answer` *where* `answer[x] = y` *if* `y` *is the least quiet person (that is, the person* `y` *with the smallest value of* `quiet[y]`*) among all people who definitely have equal to or more money than the person* `x`.

    ## Examples

    ```
    Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
    Output: [5,5,2,5,4,5,6,7]
    Explanation:
    answer[0] = 5.
    Person 5 has more money than 3, which has more money than 1, which has more money than 0.
    The only person who is quieter (has lower quiet[x]) is person 7, but it is not clear if they have more money than person 0.
    answer[7] = 7.
    Among all people that definitely have equal to or more money than person 7 (which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x]) is person 7.
    The other answers can be filled out with similar reasoning.
    ```

    ```
    Input: richer = [], quiet = [0]
    Output: [0]
    ```

    ## Constraints

    - n == quiet.length
    - 1 <= n <= 500
    - 0 <= quiet[i] < n
    - All the values of quiet are unique.
    - 0 <= richer.length <= n * (n - 1) / 2
    - 0 <= ai, bi < n
    - ai != bi
    - All the pairs of richer are unique.
    - The observations in richer are all logically consistent.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def loud_and_rich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
            raise NotImplementedError('Implement loud_and_rich')

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
