import math
from math import trunc

T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
  """Returns the estimated age of the sample in year.
  carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 
  in the sample conpared to the amount in living 
  tissue (unitless). 
  """
  if carbon_14_ratio <= 0:
      return print("Invalid entry. Must be a postive number above 0.")
  else:
      answer = math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF
      truncated_not_rounded = trunc(answer * 100) /100
      return truncated_not_rounded

# TODO: Write a unit test which feed 0.35 to the function. 
# The result should be '8680.34'. Does the function handles 
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle 
# every possible input properly. Then write a unit test againt 
# this special case.

def test_get_age_carbon_14_dating():
    carbon_14_ratio = 0.35
    assert get_age_carbon_14_dating(carbon_14_ratio) == 8680.34 
    
def test_get_neg_age_carbon_14_dating():
    carbon_14_ratio = -0.35
    assert get_age_carbon_14_dating(carbon_14_ratio) == print("Invalid entry. Must be a postive number above 0.")
    