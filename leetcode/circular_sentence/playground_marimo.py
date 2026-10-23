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
    # 2490. Circular Sentence

    **Easy** · String

    <p>A <strong>sentence</strong> is a list of words that are separated by a<strong> single</strong> space with no leading or trailing spaces.</p>

    <ul>
        <li>For example, <code>"Hello World"</code>, <code>"HELLO"</code>, <code>"hello world hello world"</code> are all sentences.</li>
    </ul>

    <p>Words consist of <strong>only</strong> uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.</p>

    <p>A sentence is <strong>circular </strong>if:</p>

    <ul>
        <li>The last character of each word in the sentence is equal to the first character of its next word.</li>
        <li>The last character of the last word is equal to the first character of the first word.</li>
    </ul>

    <p>For example, <code>"leetcode exercises sound delightful"</code>, <code>"eetcode"</code>, <code>"leetcode eats soul" </code>are all circular sentences. However, <code>"Leetcode is cool"</code>, <code>"happy Leetcode"</code>, <code>"Leetcode"</code> and <code>"I like Leetcode"</code> are <strong>not</strong> circular sentences.</p>

    <p>Given a string <code>sentence</code>, return <code>true</code><em> if it is circular</em>. Otherwise, return <code>false</code>.</p>

    ## Examples

    ```
    Input: sentence = "leetcode exercises sound delightful"
    Output: true
    Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
    - leetcode's last character is equal to exercises's first character.
    - exercises's last character is equal to sound's first character.
    - sound's last character is equal to delightful's first character.
    - delightful's last character is equal to leetcode's first character.
    The sentence is circular.
    ```

    ```
    Input: sentence = "eetcode"
    Output: true
    Explanation: The words in sentence are ["eetcode"].
    - eetcode's last character is equal to eetcode's first character.
    The sentence is circular.
    ```

    ```
    Input: sentence = "Leetcode is cool"
    Output: false
    Explanation: The words in sentence are ["Leetcode", "is", "cool"].
    - Leetcode's last character is not equal to is's first character.
    The sentence is not circular.
    ```

    ## Constraints

    - 1 &lt;= sentence.length &lt;= 500
    - sentence consist of only lowercase and uppercase English letters and spaces.
    - The words in sentence are separated by a single space.
    - There are no leading or trailing spaces.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_circular_sentence(self, sentence: str) -> bool:
            raise NotImplementedError('Implement is_circular_sentence')

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
