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
    # 528. Random Pick with Weight

    **Medium** · Array, Math, Binary Search, Prefix Sum

    You are given a **0-indexed** array of positive integers `w` where `w[i]` describes the weight of the `i^th` index.

    You need to implement the function `pick_index()`, which **randomly** picks an index in the range `[0, w.length - 1]` (**inclusive**) and returns it. The **probability** of picking an index `i` is `w[i] / sum(w)`.

    - For example, if `w = [1, 3]`, the probability of picking index `0` is `1 / (1 + 3) = 0.25` (i.e., `25%`), and the probability of picking index `1` is `3 / (1 + 3) = 0.75` (i.e., `75%`).

    ## Examples

    ```
    Input
    ["Solution","pickIndex"]
    [[[1]],[]]
    Output
    [null,0]

    Explanation
    Solution solution = new Solution([1]);
    solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
    ```

    ```
    Input
    ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    [[[1,3]],[],[],[],[],[]]
    Output
    [null,1,1,1,1,0]

    Explanation
    Solution solution = new Solution([1, 3]);
    solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
    solution.pickIndex(); // return 1
    solution.pickIndex(); // return 1
    solution.pickIndex(); // return 1
    solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

    Since this is a randomization problem, multiple answers are allowed.
    ```

    ## Constraints

    - 1 <= w.length <= 10^4
    - 1 <= w[i] <= 10^5
    - `pickIndex` will be called at most 10^4 times.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    import bisect
    import random

    class Solution:

        def __init__(self, w: list[int]) -> None:
            raise NotImplementedError('Implement __init__')

        def pick_index(self) -> int:
            raise NotImplementedError('Implement pick_index')

    practice_exports = {'bisect': bisect, 'random': random, 'Solution': Solution}
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
