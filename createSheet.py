"""
用来生成刷题列表
"""
import os
import sys
import re
from typing import List

question_pattern = re.compile(r"(\d{1,4})_(.+?)\.py")


class Question:
    def __init__(self, question_id=None, kind=None, position=None, name=None):
        self.question_id = question_id  # type:int  #题目编号
        self.kind = kind  # 题目类型
        self.link = position  # 该题所在的目录
        self.name = name

    @staticmethod
    def get_question_instance_by_base_name(base_name, kind="未归类"):

        match_result = question_pattern.match(base_name)
        if match_result:
            groups = question_pattern.match(base_name).groups()
            question_id = groups[0]
            question_name = " ".join(groups[1].split("_"))
            return Question(question_id=int(question_id), kind=kind, position="./{}/{}".format(kind, base_name),
                            name=question_name)
        else:
            return ValueError("can't parse question from path:{}".format(base_name))

    def __str__(self) -> str:
        return "id:{} name:{}  kind:{}".format(self.question_id, self.name, self.kind)


class Sheet:
    def __init__(self):
        self.abstract = "# LeetCode of Python   \n  LeetCode的Python刷题本, 不定时更新</br>\n\n\n"

        self.count = "记录题目数:"

        self.sheet_head = "| 题号 | 标题 | 题型 | 连接 |\n| :------  | :------  | :------  | :------  |\n"

    def create_sheet_md(self, items: List[Question]):
        result = []
        # 增加摘要
        result.append(self.abstract)
        result.append(self.count + str(len(items)) + "\n\n\n")
        # 增加表头
        result.append(self.sheet_head)
        # 计数

        for item in items:
            result.append(self._get_row_by_question(item))
        return "".join(result)

    def _get_row_by_question(self, q: Question):
        return "|{}|{}|{}|[链接]({})|\n".format(q.question_id, q.name, q.kind, q.link)


class Task:
    def __init__(self):
        self.sheet = None

    def start(self):
        # 用来扫描文件夹
        self.sheet = Sheet()

        container = []
        question_folder = sys.path[0]
        for item in os.listdir(question_folder):
            # item为子文件夹名
            if os.path.isdir(os.path.join(question_folder, item)) and not item.startswith("."):
                for base_name in os.listdir(os.path.join(question_folder, item)):
                    try:
                        q = Question.get_question_instance_by_base_name(base_name, item)
                        if q:
                            container.append(q)
                    except Exception as e:
                        print(e)
        # 排序
        container.sort(key=lambda x: getattr(x, "question_id"))
        content = self.sheet.create_sheet_md(container)

        # 写入README
        with open("README.md", "w") as f:
            f.write(content)
            print("更新完毕...已经刷题数:{}".format(len(container)))


if __name__ == '__main__':
    task = Task()
    task.start()
