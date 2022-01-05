

import sys
import asyncio
import itertools
# from core.aesthetics import *
from threading import Thread
from time import sleep
from typing import List


class BackgroundThread:
    def __init__(self, function, *__args, **__kwargs) -> None:
        self.function = function
        self.args = __args
        self.kwargs = __kwargs
        self.__background_thread = Thread(target=self.__run_background_thread, args=())
        self.name = self.__background_thread.name


    def __run_background_thread(self):
        self.function(*self.args, **self.kwargs)


    def start(self):
        self.__background_thread.start()


    def is_done(self):
        return not self.__background_thread.is_alive()



class SpinnerDots:
    def __init__(self, identifier: str, message: str, color: str = "yellow"):
        self.identifier = identifier
        self.message = message
        self.color = color
        self.frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.len_frames = len(self.frames)
        self.index = 0
        self.completed = False

        # self.state = f"[{green(self.identifier)}] pending ..."


    def next(self):
        if self.completed:
            return

        # self.state = f"{green(self.frames[self.index % self.len_frames])} {ConsoleColored(self.message, self.color)}"
        self.state = f"{self.frames[self.index % self.len_frames]} {self.message}"
        self.index += 1
        return self


    def done(self):
        # self.state = f"[{yellow(self.identifier)}] {green('completed')}"
        self.state = f"[{self.identifier}] {'completed'}"
        self.completed = True


    def print_state(self, __end="\r") -> str:
        print(self.state, end=__end)


    def get_state(self) -> str:
        return self.state



def background_job1(param: str):
    print(f"job 1 with '{param}' started")
    # sleep(10)
    for i in range(100_000_0000):
        pass


def background_job2(param: str):
    print(f"job 2 with '{param}' started")
    # sleep(10)
    for i in range(1_000_000_000):
        pass


def all_tasks_done(task_list: List[BackgroundThread]) -> bool:
    for task in task_list:
        if not task.is_done():
            return False
    return True



# def format_spinners(task_list, spinners_list) -> str:


def main():
    """
        this function is synchronous
    """

    spinners_list = [
        SpinnerDots("1", "its me mario", "red"),
        SpinnerDots("2", "loading time", "yellow"),
        # SpinnerDots("3", "third", "cyan"),
    ]
    tasks_list = [
        BackgroundThread(background_job1, "Andrew is here"),
        BackgroundThread(background_job2, "Andrew is NOT here"),
        BackgroundThread(background_job1, "Andrew"),
    ]

    for task in tasks_list:
        task.start()

    while 1:
        # if at least one background task is done
        # its spinner should be updated to completed
        # if all_tasks_done(tasks_list):
        #     line = ""
        #     for spinner in spinners_list:
        #         spinner.done()
        #         line += spinner.get_state() + " "
        #     print(line)

        #     break

        # total_done = 0
        # line = ""
        # for (index, spinner), task in zip(enumerate(spinners_list), tasks_list):
            # if task.is_done():
            #     total_done += 1
            #     spinners_list[index].done()
            # else:
            #     spinner.next()

            # line += spinner.get_state() + " "
            # print(line, end="\r")

        # if tasks_list[0].is_done():
        #     total_done += 1
        #     spinners_list[0].done()
        # else:
        #     spinners_list[0].next()

        # ce treaba are loading spinnerul
        # cu 2 threaduri care merg in background ?????
        # daca sunt threaduri in background
        # se misca foarte prost pentru ca aparent
        # acest while loop este influentat de cate threaduri sunt active in background
        # atata timp cat folosesti python
        # daca rulezi cu pypy3, se misca foarte bine
        print(spinners_list[0].next().get_state(), end="\r")
        sleep(0.01)


        # if total_done == len(tasks_list):
        #     break




if __name__ == '__main__':
    main()


