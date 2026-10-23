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
    # 950. Reveal Cards In Increasing Order

    **Medium** · Array, Queue, Sorting, Simulation

    <p>You are given an integer array <code>deck</code>. There is a deck of cards where every card has a unique integer. The integer on the <code>i<sup>th</sup></code> card is <code>deck[i]</code>.</p>

    <p>You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.</p>

    <p>You will do the following steps repeatedly until all cards are revealed:</p>

    <ol>
        <li>Take the top card of the deck, reveal it, and take it out of the deck.</li>
        <li>If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.</li>
        <li>If there are still unrevealed cards, go back to step 1. Otherwise, stop.</li>
    </ol>

    <p>Return <em>an ordering of the deck that would reveal the cards in <strong>increasing</strong> order</em>.</p>

    <p><strong>Note</strong> that the first entry in the answer is considered to be the top of the deck.</p>

    ## Examples

    ```
    Input: deck = [17,13,11,2,3,5,7]
    Output: [2,13,3,11,5,17,7]
    Explanation: We get the deck in the order [17,13,11,2,3,5,7] (this order does not matter), and reorder it.
    ```

    ```
    Input: deck = [1,1000]
    Output: [1,1000]
    ```

    ## Constraints

    - 1 &lt;= deck.length &lt;= 1000
    - 1 &lt;= deck[i] &lt;= 10^6
    - All the values of deck are unique.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def deck_revealed_increasing(self, deck: list[int]) -> list[int]:
            raise NotImplementedError('Implement deck_revealed_increasing')

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
