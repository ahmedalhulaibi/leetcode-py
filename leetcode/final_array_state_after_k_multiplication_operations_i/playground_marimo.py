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
    # 3264. Final Array State After K Multiplication Operations I

    **Easy** · Array, Math, Heap (Priority Queue), Simulation

    You are given an integer array `nums`, an integer `k`, and an integer `multiplier`.

    You need to perform `k` operations on `nums`. In each operation:

    - Find the **minimum** value `x` in `nums`. If there are multiple occurrences of the minimum value, select the one that appears **first**.
    - Replace the selected minimum value `x` with `x * multiplier`.

    Return an integer array denoting the final state of `nums` after performing all `k` operations.

    ## Examples

    ```
    Input: nums = [2,1,3,5,6], k = 5, multiplier = 2
    Output: [8,4,6,5,6]
    ```
    **Explanation:**

    | Operation | Result |
    | --- | --- |
    | After operation 1 | [2, 2, 3, 5, 6] |
    | After operation 2 | [4, 2, 3, 5, 6] |
    | After operation 3 | [4, 4, 3, 5, 6] |
    | After operation 4 | [4, 4, 6, 5, 6] |
    | After operation 5 | [8, 4, 6, 5, 6] |

    ```
    Input: nums = [1,2], k = 3, multiplier = 4
    Output: [16,8]
    ```
    **Explanation:**

    | Operation | Result |
    | --- | --- |
    | After operation 1 | [4, 2] |
    | After operation 2 | [4, 8] |
    | After operation 3 | [16, 8] |

    ## Constraints

    - 1 <= nums.length <= 100
    - 1 <= nums[i] <= 100
    - 1 <= k <= 10
    - 1 <= multiplier <= 5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def get_final_state(self, nums: list[int], k: int, multiplier: int) -> list[int]:
            raise NotImplementedError('Implement get_final_state')

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
