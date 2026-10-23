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
    # 751. IP to CIDR

    **Medium** · String, Bit Manipulation

    An IP address is a formatted 32-bit unsigned integer where each group of 8 bits is printed as a decimal number and the dot character `'.'` splits the groups.

    - For example, the binary number `00001111 10001000 11111111 01101011` (spaces added for clarity) formatted as an IP address would be `"15.136.255.107"`.

    A CIDR block is a format used to denote a specific set of IP addresses. It is a string consisting of a base IP address, followed by a slash, followed by a prefix length `k`. The addresses it covers are all the IPs whose first `k` bits are the same as the base IP address.

    - For example, `"123.45.67.89/20"` is a CIDR block with a prefix length of 20. Any IP address whose binary representation matches `01111011 00101101 0100xxxx xxxxxxxx`, where x can be either 0 or 1, is in the set covered by the CIDR block.

    You are given a start IP address `ip` and the number of IP addresses we need to cover `n`. Your goal is to use as few CIDR blocks as possible to cover all the IP addresses in the inclusive range `[ip, ip + n - 1]` exactly. No other IP addresses outside of the range should be covered.

    Return the shortest list of CIDR blocks that covers the range of IP addresses. If there are multiple answers, return any of them.

    ## Examples

    ```
    Input: ip = "255.0.0.7", n = 10
    Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
    Explanation: The CIDR block "255.0.0.7/32" covers the first address, "255.0.0.8/29" covers the middle 8 addresses, and "255.0.0.16/32" covers the last address.
    ```

    ```
    Input: ip = "117.145.102.62", n = 8
    Output: ["117.145.102.62/31","117.145.102.64/30","117.145.102.68/31"]
    ```

    ## Constraints

    - 7 <= ip.length <= 15
    - ip is a valid IPv4 on the form "a.b.c.d" where a, b, c, and d are integers in the range [0, 255].
    - 1 <= n <= 1000
    - Every implied address ip + x (for x < n) will be a valid IPv4 address.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def ip_to_cidr(self, ip: str, n: int) -> list[str]:
            raise NotImplementedError('Implement ip_to_cidr')

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
