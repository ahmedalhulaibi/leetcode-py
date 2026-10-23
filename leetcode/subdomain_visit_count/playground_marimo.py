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
    # 811. Subdomain Visit Count

    **Medium** · Array, Hash Table, String, Counting

    A website domain `"discuss.leetcode.com"` consists of various subdomains. At the top level, we have `"com"`, at the next level, we have `"leetcode.com"` and at the lowest level, `"discuss.leetcode.com"`. When we visit a domain like `"discuss.leetcode.com"`, we will also visit the parent domains `"leetcode.com"` and `"com"` implicitly.

    A <strong>count-paired domain</strong> is a domain that has one of the two formats `"rep d1.d2.d3"` or `"rep d1.d2"` where `rep` is the number of visits to the domain and `d1.d2.d3` is the domain itself.

    - For example, `"9001 discuss.leetcode.com"` is a <strong>count-paired domain</strong> that indicates that <code>discuss.leetcode.com</code> was visited `9001` times.

    Given an array of <strong>count-paired domains</strong> <code>cpdomains</code>, return <em>an array of the <strong>count-paired domains</strong> of each subdomain in the input</em>. You may return the answer in <strong>any order</strong>.

    ## Examples

    ```
    Input: cpdomains = ["9001 discuss.leetcode.com"]
    Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
    ```

    Explanation: We only have one website domain: `"discuss.leetcode.com"`.
    As discussed above, the subdomains `"leetcode.com"` and `"com"` will also be visited. So they will all be visited 9001 times.

    ```
    Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
    ```

    Explanation: We will visit `"google.mail.com"` 900 times, `"yahoo.com"` 50 times, `"intel.mail.com"` once and `"wiki.org"` 5 times.
    For the subdomains, we will visit `"mail.com"` 900 + 1 = 901 times, `"com"` 900 + 50 + 1 = 951 times, and `"org"` 5 times.

    ## Constraints

    - 1 <= cpdomains.length <= 100
    - 1 <= cpdomains[i].length <= 100
    - cpdomains[i] follows either the "rep<sub>i</sub> d1<sub>i</sub>.d2<sub>i</sub>.d3<sub>i</sub>" format or the "rep<sub>i</sub> d1<sub>i</sub>.d2<sub>i</sub>" format.
    - rep<sub>i</sub> is an integer in the range [1, 10<sup>4</sup>].
    - d1<sub>i</sub>, d2<sub>i</sub>, and d3<sub>i</sub> consist of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def subdomain_visits(self, cpdomains: list[str]) -> list[str]:
            raise NotImplementedError('Implement subdomain_visits')

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
