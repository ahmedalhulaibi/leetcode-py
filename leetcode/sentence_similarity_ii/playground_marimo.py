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
    # 737. Sentence Similarity II

    **Medium** · Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union Find

    We can represent a sentence as an array of words, for example, the sentence `"I am happy with leetcode"` can be represented as `arr = ["I","am","happy","with","leetcode"]`.

    Given two sentences `sentence1` and `sentence2` each represented as a string array, and given an array of string pairs `similarPairs` where `similarPairs[i] = [xi, yi]` indicates that the two words `xi` and `yi` are similar.

    Return `true` if `sentence1` and `sentence2` are similar, or `false` if they are not similar.

    Two sentences are similar if:

    - They have the **same** length (i.e., the same number of words)
    - `sentence1[i]` and `sentence2[i]` are similar.

    Notice that a word is always similar to itself, also notice that the similarity relation **is transitive**. For example, if the words `a` and `b` are similar, and the words `b` and `c` are similar, then `a` and `c` are similar.

    ## Examples

    ```
    Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
    Output: true
    Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
    ```

    ```
    Input: sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
    Output: true
    Explanation: "leetcode" -> "platform" -> "anime" -> "manga" -> "onepiece".
    ```

    ```
    Input: sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
    Output: false
    Explanation: "leetcode" is not similar to "onepiece".
    ```

    ## Constraints

    - 1 <= sentence1.length, sentence2.length <= 1000
    - 1 <= sentence1[i].length, sentence2[i].length <= 20
    - sentence1[i] and sentence2[i] consist of lower-case and upper-case English letters.
    - 0 <= similarPairs.length <= 2000
    - similarPairs[i].length == 2
    - 1 <= xi.length, yi.length <= 20
    - xi and yi consist of English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def are_sentences_similar_two(self, sentence1: list[str], sentence2: list[str], similar_pairs: list[list[str]]) -> bool:
            raise NotImplementedError('Implement are_sentences_similar_two')

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
