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
    # 271. Encode and Decode Strings

    **Medium** · Array, String, Design

    Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

    ## Examples

    ```
    Input: dummy_input = ["Hello","World"]
    Output: "Hello,World"
    Explanation: Machine 1:
    Codec encoder = new Codec();
    String msg = encoder.encode(strs);
    Machine 1 ---msg---> Machine 2
    Machine 2:
    Codec decoder = new Codec();
    String[] strs = decoder.decode(msg);
    ```

    ## Constraints

    - 1 <= strs.length <= 200
    - 0 <= strs[i].length <= 200
    - strs[i] contains any possible characters out of 256 valid ASCII characters.

    **Note:**
    - The string may contain any possible characters out of 256 valid ASCII characters. Your algorithm should be generalized enough to work on any possible characters.
    - Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
    - Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def encode(self, strs: list[str]) -> str:
            raise NotImplementedError('Implement encode')

        def decode(self, s: str) -> list[str]:
            raise NotImplementedError('Implement decode')

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
