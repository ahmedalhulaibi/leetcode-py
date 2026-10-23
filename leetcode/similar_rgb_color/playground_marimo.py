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
    # 800. Similar RGB Color

    **Easy** · Math, String, Enumeration

    The red-green-blue color `"#AABBCC"` can be written as `"#ABC"` in shorthand.

    - For example, `"#15c"` is shorthand for the color `"#1155cc"`.

    The similarity between the two colors `"#ABCDEF"` and `"#UVWXYZ"` is `-(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2`.

    Given a string `color` that follows the format `"#ABCDEF"`, return a string represents the color that is most similar to the given color and has a shorthand (i.e., it can be represented as some `"#XYZ"`).

    **Any answer** which has the same highest similarity as the best answer will be accepted.

    ## Examples

    ```
    Input: color = "#09f166"
    Output: "#11ee66"
    Explanation:
    The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
    This is the highest among any shorthand color.
    ```

    ```
    Input: color = "#4e3fe1"
    Output: "#5544dd"
    ```

    ## Constraints

    - `color.length == 7`
    - `color[0] == '#'`
    - `color[i]` is either digit or character in the range `['a', 'f']` for `i > 0`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def similar_rgb(self, color: str) -> str:
            raise NotImplementedError('Implement similar_rgb')

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
