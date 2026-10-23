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
    # 385. Mini Parser

    **Medium** · String, Stack, Depth-First Search

    Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return the deserialized `NestedInteger`.

    Each element is either an integer or a list whose elements may also be integers or other lists.

    ## Examples

    ```
    Input: s = "324"
    Output: 324
    Explanation: You should return a NestedInteger object which contains a single integer 324.
    ```

    ```
    Input: s = "[123,[456,[789]]]"
    Output: [123,[456,[789]]]
    Explanation: Return a NestedInteger object containing a nested list with 2 elements:
    1. An integer containing value 123.
    2. A nested list containing two elements:
        i.  An integer containing value 456.
        ii. A nested list with one element:
             a. An integer containing value 789
    ```

    ## Constraints

    - 1 <= s.length <= 5 * 10<sup>4</sup>
    - s consists of digits, square brackets `"[]"`, negative sign `'-'`, and commas `','`.
    - s is the serialization of valid `NestedInteger`.
    - All the values in the input are in the range [-10<sup>6</sup>, 10<sup>6</sup>].



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class NestedInteger:

        def __init__(self, value: 'int | None'=None) -> 'None':
            self._integer: 'int | None' = value
            self._list: 'list[NestedInteger] | None' = None if value is not None else []

        def is_integer(self) -> 'bool':
            return self._list is None

        def add(self, elem: 'NestedInteger') -> 'None':
            items = self._list
            if items is None:
                items = []
                self._integer = None
                self._list = items
            items.append(elem)

        def set_integer(self, value: 'int') -> 'None':
            self._integer = value
            self._list = None

        def get_integer(self) -> 'int | None':
            return self._integer

        def get_list(self) -> 'list[NestedInteger] | None':
            return self._list

    class Solution:

        def deserialize(self, s: 'str') -> 'NestedInteger':
            raise NotImplementedError('Implement deserialize')

    practice_exports = {'NestedInteger': NestedInteger, 'Solution': Solution}
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
