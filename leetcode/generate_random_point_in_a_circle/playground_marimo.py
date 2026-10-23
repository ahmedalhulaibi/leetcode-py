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
    # 478. Generate Random Point in a Circle

    **Medium** · Math, Geometry, Rejection Sampling, Randomized

    Given the radius and the position of the center of a circle, implement the function `randPoint` which generates a uniform random point inside the circle.

    Implement the `Solution` class:

    - `Solution(double radius, double x_center, double y_center)` initializes the object with the radius of the circle `radius` and the position of the center `(x_center, y_center)`.
    - `randPoint()` returns a random point inside the circle. A point on the circumference of the circle is considered to be in the circle. The answer is returned as an array `[x, y]`.

    ## Examples

    ```
    Input
    ["Solution", "randPoint", "randPoint", "randPoint"]
    [[1.0, 0.0, 0.0], [], [], []]
    Output
    [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]

    Explanation
    Solution solution = new Solution(1.0, 0.0, 0.0);
    solution.randPoint(); // return [-0.02493, -0.38077]
    solution.randPoint(); // return [0.82314, 0.38945]
    solution.randPoint(); // return [0.36572, 0.17248]
    ```

    ## Constraints

    - 0 < radius <= 10^8
    - -10^7 <= x_center, y_center <= 10^7
    - At most 3 * 10^4 calls will be made to randPoint.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    import math
    import random

    class Solution:

        def __init__(self, radius: float, x_center: float, y_center: float) -> None:
            raise NotImplementedError('Implement __init__')

        def rand_point(self) -> list[float]:
            raise NotImplementedError('Implement rand_point')

    practice_exports = {'math': math, 'random': random, 'Solution': Solution}
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
