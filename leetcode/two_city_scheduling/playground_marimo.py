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
    # 1029. Two City Scheduling

    **Medium** · Array, Greedy, Sorting

    A company is planning to interview `2n` people. Given the array `costs` where `costs[i] = [aCosti, bCosti]`, the cost of flying the `ith` person to city `a` is `aCosti`, and the cost of flying the `ith` person to city `b` is `bCosti`.

    Return *the minimum cost to fly every person to a city* such that exactly `n` people arrive in each city.

    ## Examples

    ```
    Input: costs = [[10,20],[30,200],[400,50],[30,20]]
    Output: 110
    Explanation:
    The first person goes to city A for a cost of 10.
    The second person goes to city A for a cost of 30.
    The third person goes to city B for a cost of 50.
    The fourth person goes to city B for a cost of 20.

    The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
    ```

    ```
    Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    Output: 1859
    Explanation: For example, the way to achieve the minimum of 1859 is:
    - Fly the 1st person (259, 770) to city A for 259.
    - Fly the 2nd person (448, 54) to city B for 54.
    - Fly the 3rd person (926, 667) to city B for 667.
    - Fly the 4th person (184, 139) to city B for 139.
    - Fly the 5th person (840, 118) to city B for 118.
    - Fly the 6th person (577, 469) to city A for 577.
    The total minimum cost is 1859.
    ```

    ```
    Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    Output: 3086
    Explanation: The total minimum cost is 3086.
    ```

    ## Constraints

    - `2 * n == costs.length`
    - `2 <= costs.length <= 100`
    - `costs.length` is even.
    - `1 <= aCosti, bCosti <= 1000`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def two_city_sched_cost(self, costs: list[list[int]]) -> int:
            raise NotImplementedError('Implement two_city_sched_cost')

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
