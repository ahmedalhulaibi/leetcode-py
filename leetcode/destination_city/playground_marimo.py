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
    # 1436. Destination City

    **Easy** · Array, Hash Table, String

    You are given the array `paths`, where `paths[i] = [cityA<sub>i</sub>, cityB<sub>i</sub>]` means there exists a direct path going from `cityA<sub>i</sub>` to `cityB<sub>i</sub>`. Return the destination city, that is, the city without any path outgoing to another city.

    It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

    ## Examples

    ```
    Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    Output: "Sao Paulo"
    Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
    ```

    ```
    Input: paths = [["B","C"],["D","B"],["C","A"]]
    Output: "A"
    Explanation: All possible trips are:
    "D" -> "B" -> "C" -> "A".
    "B" -> "C" -> "A".
    "C" -> "A".
    "A".
    Clearly the destination city is "A".
    ```

    ```
    Input: paths = [["A","Z"]]
    Output: "Z"
    ```

    ## Constraints

    - 1 <= paths.length <= 100
    - paths[i].length == 2
    - 1 <= cityAi.length, cityBi.length <= 10
    - cityAi != cityBi
    - All strings consist of lowercase and uppercase English letters and the space character.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def dest_city(self, paths: list[list[str]]) -> str:
            raise NotImplementedError('Implement dest_city')

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
