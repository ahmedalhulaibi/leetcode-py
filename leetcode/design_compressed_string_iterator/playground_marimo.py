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
    # 604. Design Compressed String Iterator

    **Easy** · Design, Array, String, Iterator

    Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

    Implement the `StringIterator` class:

    - `next()` Returns **the next character** if the original string still has uncompressed characters, otherwise returns a **white space**.
    - `has_next()` Returns true if there is any letter needs to be uncompressed in the original string, otherwise returns `false`.

    ## Examples

    ```
    Input
    ["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
    [["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
    Output
    [null, "L", "e", "e", "t", "C", "o", true, "d", true]

    Explanation
    StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
    stringIterator.next(); // return "L"
    stringIterator.next(); // return "e"
    stringIterator.next(); // return "e"
    stringIterator.next(); // return "t"
    stringIterator.next(); // return "C"
    stringIterator.next(); // return "o"
    stringIterator.hasNext(); // return True
    stringIterator.next(); // return "d"
    stringIterator.hasNext(); // return True
    ```

    ## Constraints

    - `1 <= compressedString.length <= 1000`
    - `compressedString` consists of lower-case an upper-case English letters and digits.
    - The number of a single character repetitions in `compressedString` is in the range `[1, 10^9]`.
    - At most `100` calls will be made to `next` and `hasNext`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class StringIterator:

        def __init__(self, compressed_string: str) -> None:
            raise NotImplementedError('Implement __init__')

        def next(self) -> str:
            raise NotImplementedError('Implement next')

        def has_next(self) -> bool:
            raise NotImplementedError('Implement has_next')

    practice_exports = {'StringIterator': StringIterator}
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
