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
    # 468. Validate IP Address

    **Medium** · String

    Given a string `queryIP`, return `"IPv4"` if IP is a valid IPv4 address, `"IPv6"` if IP is a valid IPv6 address or `"Neither"` if IP is not a correct IP of any type.

    A valid **IPv4** address is an IP in the form `"x1.x2.x3.x4"` where `0 <= xi <= 255` and `xi` **cannot contain** leading zeros. For example, `"192.168.1.1"` and `"192.168.1.0"` are valid IPv4 addresses while `"192.168.01.1"`, `"192.168.1.00"`, and `"192.168@1.1"` are invalid IPv4 addresses.

    A valid **IPv6** address is an IP in the form `"x1:x2:x3:x4:x5:x6:x7:x8"` where:

    - `1 <= xi.length <= 4`
    - `xi` is a **hexadecimal string** which may contain digits, lowercase English letters (`'a'` to `'f'`) and upper-case English letters (`'A'` to `'F'`).
    - Leading zeros are allowed in `xi`.

    For example, `"2001:0db8:85a3:0000:0000:8a2e:0370:7334"` and `"2001:db8:85a3:0:0:8A2E:0370:7334"` are valid IPv6 addresses, while `"2001:0db8:85a3::8A2E:037j:7334"` and `"02001:0db8:85a3:0000:0000:8a2e:0370:7334"` are invalid IPv6 addresses.

    ## Examples

    ```
    Input: queryIP = "172.16.254.1"
    Output: "IPv4"
    ```
    **Explanation:** This is a valid IPv4 address, return "IPv4".

    ```
    Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    Output: "IPv6"
    ```
    **Explanation:** This is a valid IPv6 address, return "IPv6".

    ```
    Input: queryIP = "256.256.256.256"
    Output: "Neither"
    ```
    **Explanation:** This is neither a IPv4 address nor a IPv6 address.

    ## Constraints

    - 1 <= queryIP.length <= 50
    - queryIP consists only of English letters, digits and the characters '.' and ':'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def valid_ip_address(self, query_ip: str) -> str:
            raise NotImplementedError('Implement valid_ip_address')

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
