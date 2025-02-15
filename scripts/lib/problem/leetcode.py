from functools import total_ordering

from lib.problem.base import Problem


@total_ordering
class LeetCodeProblem(Problem):
    def __init__(self,
                 identifier: str,
                 title: str,
                 slug: str,
                 source_type: str,
                 contest_name: str = "",
                 chapter_name: str = "",
                 difficulty: str = "",
                 is_premium: bool = False,
                 status: str = "",
                 solution_slug: str = ""):
        """
        :param identifier: a string used as a unique identifier for the problem
        :param title: Title of the problem
        :param slug: Part of url removing the common parts
        :param source_type: Practice/Contest/Explore etc?
        :param contest_name: Name of the contest in which the problem appeared.
                             Empty if source_type is not Contest
        :param chapter_name: Sub-part of the contest. Example week name in
                             Explore
        :param difficulty: Level of difficulty of the problem
        :param is_premium: Is the problem a leetcode premium?
        :param status:
        :param solution_slug: Link for leetcode solution article (if exists)
        """
        url = "https://leetcode.com/{0}problems/{1}" \
            .format(
                contest_name.lower().replace(" ", "-") + "/"
                if len(contest_name) != 0 else "",
                slug
            )
        super().__init__(
            platform="LeetCode",
            identifier=identifier,
            title=title,
            url=url,
            slug=slug,
            source_type=source_type,
            contest_name=contest_name,
            chapter_name=chapter_name,
            difficulty=difficulty,
            is_premium=is_premium
        )
        self.solution_slug = solution_slug
        self.status = status

    def __del__(self):
        pass
