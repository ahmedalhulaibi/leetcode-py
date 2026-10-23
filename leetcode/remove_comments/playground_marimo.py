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
    mo.md(r"""
    # 722. Remove Comments

    **Medium** · Array, String

    Given a C++ program, remove comments from it. The program source is an array of strings `source` where `source[i]` is the `i<sup>th</sup>` line of the source code. This represents the result of splitting the original source code string by the newline character `'\n'`.

    In C++, there are two types of comments, line comments, and block comments.

    - The string `"//"` denotes a line comment, which represents that it and the rest of the characters to the right of it in the same line should be ignored.
    - The string `"/*"` denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of `"*/"` should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string `"/*/"` does not yet end the block comment, as the ending would be overlapping the beginning.

    The first effective comment takes precedence over others.

    - For example, if the string `"//"` occurs in a block comment, it is ignored.
    - Similarly, if the string `"/*"` occurs in a line or block comment, it is also ignored.

    If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.

    There will be no control characters, single quote, or double quote characters.

    - For example, `source = "string s = "/* Not a comment. */";"` will not be a test case.

    Also, nothing else such as defines or macros will interfere with the comments.

    It is guaranteed that every open block comment will eventually be closed, so `"/*"` outside of a line or block comment always starts a new comment.

    Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.

    After removing the comments from the source code, return <em>the source code in the same format</em>.

    ## Examples

    ```
    Input: source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
    Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
    Explanation: The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments. The line by line output code is visualized as below:
    int main()
    {

    int a, b, c;
    a = b + c;
    }
    ```

    ```
    Input: source = ["a/*comment", "line", "more_comment*/b"]
    Output: ["ab"]
    Explanation: The original source string is "a/*comment\nline\nmore_comment*/b". After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].
    ```

    ## Constraints

    - 1 <= source.length <= 100
    - 0 <= source[i].length <= 80
    - source[i] consists of printable ASCII characters.
    - Every open block comment is eventually closed.
    - There are no single-quote or double-quote in the input.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def remove_comments(self, source: list[str]) -> list[str]:
            raise NotImplementedError('Implement remove_comments')

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
