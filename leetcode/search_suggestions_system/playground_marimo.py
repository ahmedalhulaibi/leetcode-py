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
    # 1268. Search Suggestions System

    **Medium** · Array, String, Binary Search, Trie, Sorting, Heap (Priority Queue)

    You are given an array of strings products and a string searchWord.

    Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

    Return a list of lists of the suggested products after each character of searchWord is typed.

    ## Examples

    ```
    Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
    Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
    Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
    After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
    After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
    ```

    ```
    Input: products = ["havana"], searchWord = "havana"
    Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
    Explanation: The only word "havana" will be always suggested while typing the search word.
    ```

    ## Constraints

    - 1 <= products.length <= 1000
    - 1 <= products[i].length <= 3000
    - 1 <= sum(products[i].length) <= 2 * 10^4
    - All the strings of products are unique.
    - products[i] consists of lowercase English letters.
    - 1 <= searchWord.length <= 1000
    - searchWord consists of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def suggested_products(self, products: list[str], search_word: str) -> list[list[str]]:
            raise NotImplementedError('Implement suggested_products')

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
