from typing import List
import logging

class JiuHua:
    def __init__(self, number=7, lights_configure=List[int]):
        if number < len(lights_configure):
            raise Exception("参数错误: lights_on.len 必须小于等于 number")
        elif number < 3:
            raise Exception("参数错误: number 必须大于等于 3")
        self.number = number
        self.lights_configure = lights_configure
        self.lights: List[int] = self.create_light_list()
        self.step = []

    def create_light_list(self):
        return [1 if i in self.lights_configure else 0 for i in range(self.number)]


    def turn(self, index: int):
        if index:
            self.step.append(index)
            self.lights[index] = 0 if self.lights[index] else 1
            self.lights[index+1] = 0 if self.lights[index+1] else 1
            self.lights[index-1] = 0 if self.lights[index-1] else 1

    def main_logic(self):
        i = 1
        while i < len(self.lights) - 1:
            if [self.lights[i-1], self.lights[i], self.lights[i+1]] == [0, 0, 0]:
                i += 1
                continue

            elif [self.lights[i-1], self.lights[i], self.lights[i+1]] == [1, 0, 0]:
                self.turn(index=i)
                i += 1
            elif [self.lights[i-1], self.lights[i], self.lights[i+1]] == [0, 0, 1]:
                self.turn(index=i+2)
                i += 3
            elif [self.lights[i-1], self.lights[i], self.lights[i+1]] == [0, 1, 0]:
                self.turn(index=i+1)
                i += 2

            elif [self.lights[i-1], self.lights[i], self.lights[i+1]] == [1, 1, 0]:
                self.turn(index=i)
                i += 2
            elif [self.lights[i-1], self.lights[i], self.lights[i+1]] == [1, 0, 1]:
                self.turn(index=i)
                i += 1
            elif [self.lights[i-1], self.lights[i], self.lights[i+1]] == [0, 1, 1]:
                self.turn(index=i+1)
                i += 3

            elif [self.lights[i-1], self.lights[i], self.lights[i+1]] == [1, 1, 1]:
                self.turn(index=i)
                i += 3

        if self.lights[-3:] in [
            [0, 0, 0,],
            [1, 0, 0,],
            [0, 1, 0,],
            [0, 0, 1,],
        ]:
            pass
        elif self.lights[-2:] in [
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 1],
            [1, 1, 1]]:
            self.step.append(len(self.lights) - 2)
        return {"result": self.lights, "step": self.step}


if __name__ == "__main__":
    jiuhua = JiuHua(number=7, lights_configure=[1,2, 4,5])
    print("original: ", jiuhua.lights)
    print(jiuhua.main_logic())