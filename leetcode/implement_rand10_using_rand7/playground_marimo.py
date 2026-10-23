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
    # 470. Implement Rand10() Using Rand7()

    **Medium** · Math, Rejection Sampling, Randomized, Probability and Statistics

    Given the **API** `rand7()` that generates a uniform random integer in the range `[1, 7]`, write a function `rand10()` that generates a uniform random integer in the range `[1, 10]`. You can only call the API `rand7()`, and you shouldn't call any other API. Please **do not** use a language's built-in random API.

    Each test case will have one **internal** argument `n`, the number of times that your implemented function `rand10()` will be called while testing. Note that this is **not an argument** passed to `rand10()`.

    ## Examples

    ```
    Input: n = 1
    Output: [2]
    ```

    ```
    Input: n = 2
    Output: [2,8]
    ```

    ```
    Input: n = 3
    Output: [3,8,10]
    ```

    ## Constraints

    - 1 <= n <= 10^5

    **Follow up:**

    - What is the expected value for the number of calls to `rand7()` function?
    - Could you minimize the number of calls to `rand7()`?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    import random

    class Rand7:

        def __init__(self, seed: int) -> None:
            self._rng = random.Random(seed)
            self.calls = 0

        def rand7(self) -> int:
            self.calls += 1
            return self._rng.randint(1, 7)

    class Solution:

        def __init__(self, rand7_api: Rand7) -> None:
            raise NotImplementedError('Implement __init__')

        def rand10(self) -> int:
            raise NotImplementedError('Implement rand10')

    practice_exports = {'random': random, 'Rand7': Rand7, 'Solution': Solution}
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
