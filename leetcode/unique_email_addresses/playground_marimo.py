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
    # 929. Unique Email Addresses

    **Easy** · Array, Hash Table, String

    <p>Every valid email consists of a local name and a domain name, separated by the <code>&#39;@&#39;</code> sign. Besides lowercase letters, the email may contain one or more <code>&#39;.&#39;</code> or <code>&#39;+&#39;</code>.</p>

    <ul>
        <li>For example, in <code>&quot;alice@leetcode.com&quot;</code>, <code>&quot;alice&quot;</code> is the <strong>local name</strong>, and <code>&quot;leetcode.com&quot;</code> is the <strong>domain name</strong>.</li>
    </ul>

    <p>If you add periods <code>&#39;.&#39;</code> between some characters in the <strong>local name</strong> part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule <strong>does not apply</strong> to domain names.</p>

    <ul>
        <li>For example, <code>&quot;alice.z@leetcode.com&quot;</code> and <code>&quot;alicez@leetcode.com&quot;</code> forward to the same email address.</li>
    </ul>

    <p>If you add a plus <code>&#39;+&#39;</code> in the <strong>local name</strong>, everything after the first plus sign will be <strong>ignored</strong>. This allows certain emails to be filtered. Note that this rule <strong>does not apply</strong> to domain names.</p>

    <ul>
        <li>For example, <code>&quot;m.y+name@email.com&quot;</code> will be forwarded to <code>&quot;my@email.com&quot;</code>.</li>
    </ul>

    <p>It is possible to use both of these rules at the same time.</p>

    <p>Given an array of strings <code>emails</code> where we send one email to each <code>emails[i]</code>, return <em>the number of different addresses that actually receive mails</em>.</p>

    ## Examples

    ```
    Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    Output: 2
    Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
    ```

    ```
    Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    Output: 3
    Explanation: All three addresses actually receive mails.
    ```

    ## Constraints

    - 1 &lt;= emails.length &lt;= 100
    - 1 &lt;= emails[i].length &lt;= 100
    - emails[i] consist of lowercase English letters, &#39;+&#39;, &#39;.&#39; and &#39;@&#39;.
    - Each emails[i] contains exactly one &#39;@&#39; character.
    - All local and domain names are non-empty.
    - Local names do not start with a &#39;+&#39; character.
    - Domain names end with the &quot;.com&quot; suffix.
    - Domain names must contain at least one character before &quot;.com&quot; suffix.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_unique_emails(self, emails: list[str]) -> int:
            raise NotImplementedError('Implement num_unique_emails')

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
