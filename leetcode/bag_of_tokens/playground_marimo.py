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
    # 948. Bag of Tokens

    **Medium** · Array, Two Pointers, Greedy, Sorting

    <p>You start with an initial power of <code>power</code>, an initial score of <code>0</code>, and a bag of tokens given as an integer array <code>tokens</code>, where each&nbsp;<code>tokens[i]</code> denotes the value of token<sub>i</sub>.</p>

    <p>Your goal is to maximize the total <strong>score</strong> by strategically playing these tokens. In one move, you can play an <strong>unplayed</strong> token in one of the two ways (but not both for the same token):</p>

    <ul>
        <li><strong>Face-up:</strong> If your current power is at least <code>tokens[i]</code>, you may play token<sub>i</sub>, losing <code>tokens[i]</code> power and gaining <code>1</code> score.</li>
        <li><strong>Face-down:</strong> If your current score is at least <code>1</code>, you may play token<sub>i</sub>, gaining <code>tokens[i]</code> power and losing <code>1</code> score.</li>
    </ul>

    <p>Return <em>the maximum possible <strong>score</strong> you can achieve after playing any number of tokens</em>.</p>

    ## Examples

    ```
    Input: tokens = [100], power = 50
    Output: 0
    Explanation: Since your score is 0 initially, you cannot play the token face-down. You also cannot play it face-up since your power (50) is less than tokens[0] (100).
    ```

    ```
    Input: tokens = [200,100], power = 150
    Output: 1
    Explanation: Play token1 (100) face-up, reducing your power to 50 and increasing your score to 1.
    ```

    ```
    Input: tokens = [100,200,300,400], power = 200
    Output: 2
    Explanation: Play the tokens in this order to get a score of 2:
    Play token0 (100) face-up, reducing power to 100 and increasing score to 1.
    Play token3 (400) face-down, increasing power to 500 and reducing score to 0.
    Play token1 (200) face-up, reducing power to 300 and increasing score to 1.
    Play token2 (300) face-up, reducing power to 0 and increasing score to 2.
    ```

    ## Constraints

    - 0 &lt;= tokens.length &lt;= 1000
    - 0 &lt;= tokens[i], power &lt; 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def bag_of_tokens_score(self, tokens: list[int], power: int) -> int:
            raise NotImplementedError('Implement bag_of_tokens_score')

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
