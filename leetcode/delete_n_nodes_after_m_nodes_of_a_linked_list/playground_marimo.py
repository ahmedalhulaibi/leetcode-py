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
    # 1474. Delete N Nodes After M Nodes of a Linked List

    **Easy** · Linked List

    You are given the `head` of a linked list and two integers `m` and `n`.

    Traverse the linked list and remove some nodes in the following way:

    - Start with the head as the current node.
    - Keep the first `m` nodes starting with the current node.
    - Remove the next `n` nodes
    - Keep repeating steps 2 and 3 until you reach the end of the list.

    Return *the head of the modified list after removing the mentioned nodes*.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1474.Delete%20N%20Nodes%20After%20M%20Nodes%20of%20a%20Linked%20List/images/sample_1_1848.png)

    ```
    Input: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
    Output: [1,2,6,7,11,12]
    Explanation: Keep the first (m = 2) nodes starting from the head of the linked List (1 -> 2) show in black nodes.
    Delete the next (n = 3) nodes (3 -> 4 -> 5) show in red nodes.
    Continue with the same procedure until reaching the tail of the Linked List.
    Head of the linked list after removing nodes is returned.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1474.Delete%20N%20Nodes%20After%20M%20Nodes%20of%20a%20Linked%20List/images/sample_2_1848.png)

    ```
    Input: head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
    Output: [1,5,9]
    Explanation: Head of linked list after removing nodes is returned.
    ```

    ## Constraints

    - The number of nodes in the list is in the range `[1, 10^4]`.
    - `1 <= Node.val <= 10^6`
    - `1 <= m, n <= 1000`

    **Follow up:** Could you solve this problem by modifying the list in-place?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def delete_nodes(self, head: ListNode[int] | None, m: int, n: int) -> ListNode[int] | None:
            raise NotImplementedError('Implement delete_nodes')

    practice_exports = {'ListNode': ListNode, 'Solution': Solution}
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
