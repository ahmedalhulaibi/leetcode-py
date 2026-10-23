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
    # 710. Random Pick with Blacklist

    **Hard** · Array, Hash Table, Math, Binary Search, Sorting, Randomized

    You are given an integer `n` and an array of **unique** integers `blacklist`. Design an algorithm to pick a random integer in the range `[0, n - 1]` that is **not** in `blacklist`. Any integer that is in the mentioned range and not in `blacklist` should be **equally likely** to be returned.

    Optimize your algorithm such that it minimizes the number of calls to the **built-in** random function of your language.

    Implement the `Solution` class:

    - `Solution(int n, int[] blacklist)` Initializes the object with the integer `n` and the blacklisted integers `blacklist`.
    - `int pick()` Returns a random integer in the range `[0, n - 1]` and not in `blacklist`.

    ## Examples

    ```
    Input
    ["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
    [[7, [2, 3, 5]], [], [], [], [], [], [], []]
    Output
    [null, 0, 4, 1, 6, 1, 0, 4]

    Explanation
    Solution solution = new Solution(7, [2, 3, 5]);
    solution.pick(); // return 0, any integer from [0,1,4,6] should be ok. Note that for every call of pick,
                     // 0, 1, 4, and 6 must be equally likely to be returned (i.e., with probability 1/4).
    solution.pick(); // return 4
    solution.pick(); // return 1
    solution.pick(); // return 6
    solution.pick(); // return 1
    solution.pick(); // return 0
    solution.pick(); // return 4
    ```

    ## Constraints

    - `1 <= n <= 10^9`
    - `0 <= blacklist.length <= min(10^5, n - 1)`
    - `0 <= blacklist[i] < n`
    - All the values of `blacklist` are **unique**.
    - At most `2 * 10^4` calls will be made to `pick`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def __init__(self, n: int, blacklist: list[int]) -> None:
            raise NotImplementedError('Implement __init__')

        def pick(self) -> int:
            raise NotImplementedError('Implement pick')

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
