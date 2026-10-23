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
    # 2570. Merge Two 2D Arrays by Summing Values

    **Easy** · Array, Hash Table, Two Pointers

    You are given two <strong>2D</strong> integer arrays <code>nums1</code> and <code>nums2</code>.

    - <code>nums1[i] = [id<sub>i</sub>, val<sub>i</sub>]</code> indicate that the number with the id <code>id<sub>i</sub></code> has a value equal to <code>val<sub>i</sub></code>.
    - <code>nums2[i] = [id<sub>i</sub>, val<sub>i</sub>]</code> indicate that the number with the id <code>id<sub>i</sub></code> has a value equal to <code>val<sub>i</sub></code>.

    Each array contains <strong>unique</strong> ids and is sorted in <strong>ascending</strong> order by id.

    Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

    - Only ids that appear in at least one of the two arrays should be included in the resulting array.
    - Each id should be included <strong>only once</strong> and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be <code>0</code>.

    Return <em>the resulting array</em>. The returned array must be sorted in ascending order by id.

    ## Examples

    ```
    Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
    Output: [[1,6],[2,3],[3,2],[4,6]]
    Explanation: The resulting array contains the following:
    - id = 1, the value of this id is 2 + 4 = 6.
    - id = 2, the value of this id is 3.
    - id = 3, the value of this id is 2.
    - id = 4, the value of this id is 5 + 1 = 6.
    ```

    ```
    Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
    Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
    Explanation: There are no common ids, so we just include each id with its value in the resulting list.
    ```

    ## Constraints

    - 1 <= nums1.length, nums2.length <= 200
    - nums1[i].length == nums2[j].length == 2
    - 1 <= id<sub>i</sub>, val<sub>i</sub> <= 1000
    - Both arrays contain unique ids.
    - Both arrays are in strictly ascending order by id.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def merge_arrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
            raise NotImplementedError('Implement merge_arrays')

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
