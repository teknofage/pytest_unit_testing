import Grades
import pandas as pd

def test_calculate_stat():
    grade_list = [6,6,6,7,8,10]
    assert calculate_stat(grade_list) == pd.mean(grade_list), pd.sd(grade_list)