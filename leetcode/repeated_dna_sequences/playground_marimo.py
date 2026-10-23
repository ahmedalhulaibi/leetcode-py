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
    # 187. Repeated DNA Sequences

    **Medium** · Hash Table, String, Bit Manipulation, Sliding Window, Rolling Hash, Hash Function

    The **DNA sequence** is composed of a series of nucleotides abbreviated as `'A'`, `'C'`, `'G'`, and `'T'`.

    - For example, `"ACGAATTCCG"` is a **DNA sequence**.

    When studying **DNA**, it is useful to identify repeated sequences within the DNA.

    Given a string `s` that represents a DNA sequence, return all the **10-letter-long sequences** (substrings) that occur more than once in a DNA molecule. You may return the answer in **any order**.

    ## Examples

    ```
    Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    Output: ["AAAAACCCCC","CCCCCAAAAA"]
    ```

    ```
    Input: s = "AAAAAAAAAAAAA"
    Output: ["AAAAAAAAAA"]
    ```

    ## Constraints

    - 1 <= s.length <= 10<sup>5</sup>
    - `s[i]` is either `'A'`, `'C'`, `'G'`, or `'T'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def repeated_dna_sequences(self, s: str) -> list[str]:
            raise NotImplementedError('Implement repeated_dna_sequences')

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
