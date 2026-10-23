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
    # 444. Sequence Reconstruction

    **Medium** · Graph, Topological Sort, Array, Directed Acyclic Graph

    You are given an integer array `nums` of length `n` where `nums` is a permutation of the integers in the range `[1, n]`. You are also given a 2D integer array `sequences` where `sequences[i]` is a subsequence of `nums`.

    Check if `nums` is the shortest possible and the only **supersequence**. The shortest **supersequence** is a sequence **with the shortest length** and has all `sequences[i]` as subsequences. There could be multiple valid **supersequences** for the given array `sequences`.

    - For example, for `sequences = [[1,2],[1,3]]`, there are two shortest **supersequences**, `[1,2,3]` and `[1,3,2]`.
    - While for `sequences = [[1,2],[1,3],[1,2,3]]`, the only shortest **supersequence** possible is `[1,2,3]`. `[1,2,3,4]` is a possible supersequence but not the shortest.

    Return `true` if `nums` is the only shortest **supersequence** for `sequences`, or `false` otherwise.

    A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

    ## Examples

    ```
    Input: nums = [1,2,3], sequences = [[1,2],[1,3]]
    Output: false
    Explanation: There are two possible supersequences: [1,2,3] and [1,3,2]. Since nums is not the only shortest supersequence, we return false.
    ```

    ```
    Input: nums = [1,2,3], sequences = [[1,2]]
    Output: false
    Explanation: The shortest possible supersequence is [1,2]. Since nums is not the shortest supersequence, we return false.
    ```

    ```
    Input: nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]
    Output: true
    Explanation: The shortest possible supersequence is [1,2,3]. Since nums is the only shortest supersequence, we return true.
    ```

    ## Constraints

    - `n == nums.length`
    - `1 <= n <= 10^4`
    - `nums` is a permutation of all the integers in the range `[1, n]`.
    - `1 <= sequences.length <= 10^4`
    - `1 <= sequences[i].length <= 10^4`
    - `1 <= sum(sequences[i].length) <= 10^5`
    - `1 <= sequences[i][j] <= n`
    - All the arrays of `sequences` are **unique**.
    - `sequences[i]` is a subsequence of `nums`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def sequence_reconstruction(self, nums: list[int], sequences: list[list[int]]) -> bool:
            raise NotImplementedError('Implement sequence_reconstruction')

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
