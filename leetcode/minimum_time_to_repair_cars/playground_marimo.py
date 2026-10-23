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
    # 2594. Minimum Time to Repair Cars

    **Medium** · Array, Binary Search

    You are given an integer array <code>ranks</code> representing the <strong>ranks</strong> of some mechanics. <code>ranks[i]</code> is the rank of the <code>i<sup>th</sup></code> mechanic. A mechanic with a rank <code>r</code> can repair <code>n</code> cars in <code>r * n<sup>2</sup></code> minutes.

    You are also given an integer <code>cars</code> representing the total number of cars waiting in the garage to be repaired.

    Return <em>the <strong>minimum</strong> time taken to repair all the cars.</em>

    <strong>Note:</strong> All the mechanics can repair the cars simultaneously.

    ## Examples

    ```
    Input: ranks = [4,2,3,1], cars = 10
    Output: 16
    Explanation:
    - The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
    - The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
    - The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
    - The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
    It can be proved that the cars cannot be repaired in less than 16 minutes.
    ```

    ```
    Input: ranks = [5,1,8], cars = 6
    Output: 16
    Explanation:
    - The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
    - The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
    - The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
    It can be proved that the cars cannot be repaired in less than 16 minutes.
    ```

    ## Constraints

    - 1 <= ranks.length <= 10<sup>5</sup>
    - 1 <= ranks[i] <= 100
    - 1 <= cars <= 10<sup>6</sup>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def repair_cars(self, ranks: list[int], cars: int) -> int:
            raise NotImplementedError('Implement repair_cars')

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
