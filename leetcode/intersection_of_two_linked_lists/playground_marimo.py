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
    # 160. Intersection of Two Linked Lists

    **Easy** · Hash Table, Linked List, Two Pointers

    Given the heads of two singly linked-lists `headA` and `headB`, return *the node at which the two lists intersect*. If the two linked lists have no intersection at all, return `null`.

    For example, the following two linked lists begin to intersect at node `c1`:

    ![Intersection Statement](https://assets.leetcode.com/uploads/2021/03/05/160_statement.png)

    The test cases are generated such that there are no cycles anywhere in the entire linked structure.

    **Note** that the linked lists must **retain their original structure** after the function returns.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png)

    ```
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    Output: Intersected at '8'
    Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
    From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
    - Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png)

    ```
    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    Output: Intersected at '2'
    Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
    From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/03/05/160_example_3.png)

    ```
    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    Output: No intersection
    Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
    ```

    ## Constraints

    - The number of nodes of `listA` is in the `m`
    - The number of nodes of `listB` is in the `n`
    - 1 <= m, n <= 3 * 10^4
    - 1 <= Node.val <= 10^5
    - 0 <= skipA <= m
    - 0 <= skipB <= n
    - `intersectVal` is `0` if `listA` and `listB` do not intersect.
    - `intersectVal == listA[skipA] == listB[skipB]` if `listA` and `listB` intersect.

    **Follow up:** Could you write a solution that runs in `O(m + n)` time and use only `O(1)` memory?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def get_intersection_node(self, head_a: ListNode[int] | None, head_b: ListNode[int] | None) -> ListNode[int] | None:
            raise NotImplementedError('Implement get_intersection_node')

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
