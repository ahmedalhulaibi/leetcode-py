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
    # 535. Encode and Decode TinyURL

    **Medium** · Hash Table, String, Design

    TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl` and it returns a short URL such as `http://tinyurl.com/4e9iAk`. Design a class to encode a URL and decode a tiny URL.

    > Note: This is a companion problem to the System Design problem: Design TinyURL.

    There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

    Implement the `Codec` class:

    - `Codec()` Initializes the object of the system.
    - `String encode(String longUrl)` Returns a tiny URL for the given `longUrl`.
    - `String decode(String shortUrl)` Returns the original long URL for the given `shortUrl`. It is guaranteed that the given `shortUrl` was encoded by the same object.

    ## Examples

    ```
    Input: url = "https://leetcode.com/problems/design-tinyurl"
    Output: "https://leetcode.com/problems/design-tinyurl"

    Explanation:
    Codec codec = new Codec();
    string tiny = codec.encode(url); // returns the encoded tiny url.
    string ans = codec.decode(tiny); // returns the original url after decoding it.
    ```

    ## Constraints

    - `1 <= url.length <= 10^4`
    - `url` is guranteed to be a valid URL.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Codec:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def encode(self, long_url: str) -> str:
            raise NotImplementedError('Implement encode')

        def decode(self, short_url: str) -> str:
            raise NotImplementedError('Implement decode')

    practice_exports = {'Codec': Codec}
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
