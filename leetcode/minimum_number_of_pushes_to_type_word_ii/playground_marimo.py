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
    # 3016. Minimum Number of Pushes to Type Word II

    **Medium** · Hash Table, String, Greedy, Sorting, Counting

    You are given a string `word` containing lowercase English letters.

    Telephone keypads have keys mapped with **distinct** collections of lowercase English letters, which can be used to form words by pushing them. For example, the key `2` is mapped with `["a","b","c"]`, we need to push the key one time to type `"a"`, two times to type `"b"`, and three times to type `"c"` .

    It is allowed to remap the keys numbered `2` to `9` to **distinct** collections of letters. The keys can be remapped to **any** amount of letters, but each letter **must** be mapped to **exactly** one key. You need to find the **minimum** number of times the keys will be pushed to type the string `word`.

    Return *the **minimum** number of pushes needed to type* `word` *after remapping the keys*.

    An example mapping of letters to keys on a telephone keypad is given below. Note that `1`, `*`, `#`, and `0` do **not** map to any letters.

    ![Keypad](https://assets.leetcode.com/uploads/2023/12/26/keypaddesc.png)

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2023/12/26/keypadv1e1.png)

    ```
    Input: word = "abcde"
    Output: 5
    Explanation: The remapped keypad given in the image provides the minimum cost.
    "a" -> one push on key 2
    "b" -> one push on key 3
    "c" -> one push on key 4
    "d" -> one push on key 5
    "e" -> one push on key 6
    Total cost is 1 + 1 + 1 + 1 + 1 = 5.
    It can be shown that no other mapping can provide a lower cost.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2024/08/20/edited.png)

    ```
    Input: word = "xyzxyzxyzxyz"
    Output: 12
    Explanation: The remapped keypad given in the image provides the minimum cost.
    "x" -> one push on key 2
    "y" -> one push on key 3
    "z" -> one push on key 4
    Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
    It can be shown that no other mapping can provide a lower cost.
    Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2023/12/27/keypadv2.png)

    ```
    Input: word = "aabbccddeeffgghhiiiiii"
    Output: 24
    Explanation: The remapped keypad given in the image provides the minimum cost.
    "a" -> one push on key 2
    "b" -> one push on key 3
    "c" -> one push on key 4
    "d" -> one push on key 5
    "e" -> one push on key 6
    "f" -> one push on key 7
    "g" -> one push on key 8
    "h" -> two pushes on key 9
    "i" -> one push on key 9
    Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.
    It can be shown that no other mapping can provide a lower cost.
    ```

    ## Constraints

    - `1 <= word.length <= 10^5`
    - `word` consists of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_pushes(self, word: str) -> int:
            raise NotImplementedError('Implement minimum_pushes')

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
