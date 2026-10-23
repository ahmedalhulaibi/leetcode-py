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
    # 514. Freedom Trail

    **Hard** · String, Dynamic Programming, Depth-First Search, Breadth-First Search

    In the video game Fallout 4, the quest *"Road to Freedom"* requires players to reach a metal dial called the **"Freedom Trail Ring"** and use the dial to spell a specific keyword to open the door.

    Given a string `ring` that represents the code engraved on the outer ring and another string `key` that represents the keyword that needs to be spelled, return *the minimum number of steps to spell all the characters in the keyword*.

    Initially, the first character of the ring is aligned at the `"12:00"` direction. You should spell all the characters in `key` one by one by rotating `ring` clockwise or anticlockwise to make each character of the string key aligned at the `"12:00"` direction and then by pressing the center button.

    At the stage of rotating the ring to spell the key character `key[i]`:

    1. You can rotate the ring clockwise or anticlockwise by one place, which counts as **one step**. The final purpose of the rotation is to align one of `ring`'s characters at the `"12:00"` direction, where this character must equal `key[i]`.
    2. If the character `key[i]` has been aligned at the `"12:00"` direction, press the center button to spell, which also counts as **one step**. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2024/09/17/ring.jpg)

    ```
    Input: ring = "godding", key = "gd"
    Output: 4
    Explanation:
    For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
    For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
    Also, we need 1 more step for spelling.
    So the final output is 4.
    ```

    ```
    Input: ring = "godding", key = "godding"
    Output: 13
    ```

    ## Constraints

    - `1 <= ring.length, key.length <= 100`
    - `ring` and `key` consist of only lower case English letters.
    - It is guaranteed that `key` could always be spelled by rotating `ring`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_rotate_steps(self, ring: str, key: str) -> int:
            raise NotImplementedError('Implement find_rotate_steps')

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
