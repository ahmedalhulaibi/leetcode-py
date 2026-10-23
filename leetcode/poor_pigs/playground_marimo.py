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
    # 458. Poor Pigs

    **Hard** · Math, Dynamic Programming, Combinatorics

    There are `buckets` buckets of liquid, where **exactly one** of the buckets is poisonous. To figure out which one is poisonous, you feed some number of (poor) pigs the liquid to see whether they will die or not. Unfortunately, you only have `minutesToTest` minutes to determine which bucket is poisonous.

    You can feed the pigs according to these steps:

    1. Choose some live pigs to feed.
    2. For each pig, choose which buckets to feed it. The pig will consume all the chosen buckets simultaneously and will take no time. Each pig can feed from any number of buckets, and each bucket can be fed from by any number of pigs.
    3. Wait for `minutesToDie` minutes. You may **not** feed any other pigs during this time.
    4. After `minutesToDie` minutes have passed, any pigs that have been fed the poisonous bucket will die, and all others will survive.
    5. Repeat this process until you run out of time.

    Given `buckets`, `minutesToDie`, and `minutesToTest`, return the **minimum** number of pigs needed to figure out which bucket is poisonous within the allotted time.

    ## Examples

    ```
    Input: buckets = 4, minutesToDie = 15, minutesToTest = 15
    Output: 2
    Explanation: We can determine the poisonous bucket as follows:
    At time 0, feed the first pig buckets 1 and 2, and feed the second pig buckets 2 and 3.
    At time 15, there are 4 possible outcomes:
    - If only the first pig dies, then bucket 1 must be poisonous.
    - If only the second pig dies, then bucket 3 must be poisonous.
    - If both pigs die, then bucket 2 must be poisonous.
    - If neither pig dies, then bucket 4 must be poisonous.
    ```

    ```
    Input: buckets = 4, minutesToDie = 15, minutesToTest = 30
    Output: 2
    Explanation: We can determine the poisonous bucket as follows:
    At time 0, feed the first pig bucket 1, and feed the second pig bucket 2.
    At time 15, there are 2 possible outcomes:
    - If either pig dies, then the poisonous bucket is the one it was fed.
    - If neither pig dies, then feed the first pig bucket 3, and feed the second pig bucket 4.
    At time 30, one of the two pigs must die, and the poisonous bucket is the one it was fed.
    ```

    ## Constraints

    - 1 <= buckets <= 1000
    - 1 <= minutesToDie <= minutesToTest <= 100



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def poor_pigs(self, buckets: int, minutes_to_die: int, minutes_to_test: int) -> int:
            raise NotImplementedError('Implement poor_pigs')

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
