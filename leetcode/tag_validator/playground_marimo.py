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
    # 591. Tag Validator

    **Hard** · String, Stack

    Given a string representing a code snippet, implement a tag validator to parse the code and return whether it is valid.

    A code snippet is valid if all the following rules hold:

    1. The code must be wrapped in a **valid closed tag**. Otherwise, the code is invalid.
    2. A **closed tag** (not necessarily valid) has exactly the following format : `<TAG_NAME>TAG_CONTENT</TAG_NAME>`. Among them, `<TAG_NAME>` is the start tag, and `</TAG_NAME>` is the end tag. The TAG_NAME in start and end tags should be the same. A closed tag is **valid** if and only if the TAG_NAME and TAG_CONTENT are valid.
    3. A **valid** `TAG_NAME` only contain **upper-case letters**, and has length in range [1,9]. Otherwise, the `TAG_NAME` is **invalid**.
    4. A **valid** `TAG_CONTENT` may contain other **valid closed tags**, **cdata** and any characters (see note1) **EXCEPT** unmatched `<`, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the `TAG_CONTENT` is invalid.
    5. A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
    6. A `<` is unmatched if you cannot find a subsequent `>`. And when you find a `<` or `</`, all the subsequent characters until the next `>` should be parsed as TAG_NAME (not necessarily valid).
    7. The cdata has the following format : `<![CDATA[CDATA_CONTENT]]>`. The range of `CDATA_CONTENT` is defined as the characters between `<![CDATA[` and the **first subsequent** `]]>`.
    8. `CDATA_CONTENT` may contain **any characters**. The function of cdata is to forbid the validator to parse `CDATA_CONTENT`, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as **regular characters**.

    ## Examples

    ```
    Input: code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
    Output: true
    Explanation:
    The code is wrapped in a closed tag : <DIV> and </DIV>.
    The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata.
    Although CDATA_CONTENT has an unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as a tag.
    So TAG_CONTENT is valid, and then the code is valid. Thus return true.
    ```

    ```
    Input: code = "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"
    Output: true
    Explanation:
    We first separate the code into : start_tag|tag_content|end_tag.
    start_tag -> "<DIV>"
    end_tag -> "</DIV>"
    tag_content could also be separated into : text1|cdata|text2.
    text1 -> ">>  ![cdata[]] "
    cdata -> "<![CDATA[<div>]>]]>", where the CDATA_CONTENT is "<div>]>"
    text2 -> "]]>>]"
    The reason why start_tag is NOT "<DIV>>>" is because of the rule 6.
    The reason why cdata is NOT "<![CDATA[<div>]>]]>]]>" is because of the rule 7.
    ```

    ```
    Input: code = "<A>  <B> </A>   </B>"
    Output: false
    Explanation: Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.
    ```

    ## Constraints

    - 1 <= code.length <= 500
    - code consists of English letters, digits, '<', '>', '/', '!', '[', ']', '.', and ' '.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_valid(self, code: str) -> bool:
            raise NotImplementedError('Implement is_valid')

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
