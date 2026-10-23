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
    # 640. Solve the Equation

    **Medium** · Math, String, Simulation, Linear Algebra

    Solve a given equation and return the value of `x` in the form of a string `"x=#value"`. The equation contains only `'+'`, `'-'` operation, the variable `x` and its coefficient. You should return `"No solution"` if there is no solution for the equation, or `"Infinite solutions"` if there are infinite solutions for the equation.

    If there is exactly one solution for the equation, we ensure that the value of `x` is an integer.

    ## Examples

    ```
    Input: equation = "x+5-3+x=6+x-2"
    Output: "x=2"
    ```

    ```
    Input: equation = "x=x"
    Output: "Infinite solutions"
    ```

    ```
    Input: equation = "2x=x"
    Output: "x=0"
    ```

    ## Constraints

    - 3 <= equation.length <= 1000
    - equation has exactly one '='.
    - equation consists of integers with an absolute value in the range [0, 100] without any leading zeros, and the variable 'x'.
    - The input is generated that if there is a single solution, it will be an integer.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def solve_equation(self, equation: str) -> str:
            raise NotImplementedError('Implement solve_equation')

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
