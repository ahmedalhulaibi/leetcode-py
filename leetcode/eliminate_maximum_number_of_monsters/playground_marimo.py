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
    # 1921. Eliminate Maximum Number of Monsters

    **Medium** · Array, Greedy, Sorting

    You are playing a video game where you are defending your city from a group of `n` monsters. You are given a **0-indexed** integer array `dist` of size `n`, where `dist[i]` is the **initial distance** in kilometers of the `i`th monster from the city.

    The monsters walk toward the city at a **constant** speed. The speed of each monster is given to you in an integer array `speed` of size `n`, where `speed[i]` is the speed of the `i`th monster in kilometers per minute.

    You have a weapon that, once fully charged, can eliminate a **single** monster. However, the weapon takes **one minute** to charge. The weapon is fully charged at the very start.

    You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is fully charged, it counts as a **loss**, and the game ends before you can use your weapon.

    Return the maximum number of monsters that you can eliminate before you lose, or `n` if you can eliminate all the monsters before they reach the city.

    ## Examples

    ```
    Input: dist = [1,3,4], speed = [1,1,1]
    Output: 3
    Explanation:
    In the beginning, the distances of the monsters are [1,3,4]. You eliminate the first monster.
    After a minute, the distances of the monsters are [X,2,3]. You eliminate the second monster.
    After a minute, the distances of the monsters are [X,X,2]. You eliminate the third monster.
    All 3 monsters can be eliminated.
    ```

    ```
    Input: dist = [1,1,2,3], speed = [1,1,1,1]
    Output: 1
    Explanation:
    In the beginning, the distances of the monsters are [1,1,2,3]. You eliminate the first monster.
    After a minute, the distances of the monsters are [X,0,1,2], so you lose.
    You can only eliminate 1 monster.
    ```

    ```
    Input: dist = [3,2,4], speed = [5,3,2]
    Output: 1
    Explanation:
    In the beginning, the distances of the monsters are [3,2,4]. You eliminate the first monster.
    After a minute, the distances of the monsters are [X,0,2], so you lose.
    You can only eliminate 1 monster.
    ```

    ## Constraints

    - n == dist.length == speed.length
    - 1 <= n <= 10^5
    - 1 <= dist[i], speed[i] <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def eliminate_maximum(self, dist: list[int], speed: list[int]) -> int:
            raise NotImplementedError('Implement eliminate_maximum')

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
