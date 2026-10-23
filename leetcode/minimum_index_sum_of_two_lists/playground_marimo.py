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
    # 599. Minimum Index Sum of Two Lists

    **Easy** · Array, Hash Table, String

    Given two arrays of strings `list1` and `list2`, find the **common strings with the least index sum**.

    A **common string** is a string that appeared in both `list1` and `list2`.

    A **common string with the least index sum** is a common string such that if it appeared at `list1[i]` and `list2[j]` then `i + j` should be the minimum value among all the other **common strings**.

    Return *all the **common strings with the least index sum***. Return the answer in **any order**.

    ## Examples

    ```
    Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    Output: ["Shogun"]
    Explanation: The only common string is "Shogun".
    ```

    ```
    Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
    Output: ["Shogun"]
    Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
    ```

    ```
    Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
    Output: ["sad","happy"]
    Explanation: There are three common strings:
    "happy" with index sum = (0 + 1) = 1.
    "sad" with index sum = (1 + 0) = 1.
    "good" with index sum = (2 + 2) = 4.
    The strings with the least index sum are "sad" and "happy".
    ```

    ## Constraints

    - 1 <= list1.length, list2.length <= 1000
    - 1 <= list1[i].length, list2[i].length <= 30
    - list1[i] and list2[i] consist of spaces ' ' and English letters.
    - All the strings of list1 are unique.
    - All the strings of list2 are unique.
    - There is at least a common string between list1 and list2.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_restaurant(self, list1: list[str], list2: list[str]) -> list[str]:
            raise NotImplementedError('Implement find_restaurant')

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
