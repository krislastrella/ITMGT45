{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "b66c4b49",
   "metadata": {},
   "outputs": [],
   "source": [
    "def savings(gross_pay, tax_rate, expenses):\n",
    "    '''Savings.\n",
    "    2 points.\n",
    "    This function calculates the money remaining\n",
    "        for an employee after taxes and expenses.\n",
    "    \n",
    "    To get the take-home pay of an employee, we will\n",
    "        follow the following process:\n",
    "        1. Apply the tax rate to the gross pay of the employee; round down\n",
    "        2. Subtract the expenses from the after-tax pay of the employee\n",
    "    Parameters\n",
    "    ----------\n",
    "    gross_pay: int\n",
    "        the gross pay of an employee for a certain time period, expressed in centavos\n",
    "    tax_rate: float\n",
    "        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)\n",
    "    expenses: int\n",
    "        the expenses of an employee for a certain time period, expressed in centavos\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the number of centavos remaining from an employee's pay after taxes and expenses\n",
    "    '''\n",
    "    # Replace `pass` with your code. \n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    tax = (gross_pay*(tax_rate))//1\n",
    "    income= gross_pay-tax\n",
    "    takehomepay = tax-expenses\n",
    "    return (takehomepay)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "8845cf0a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "120.7"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "savings(1234.578,.2,125.30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5d9ab860",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'10kg'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def material_waste(total_material, material_units, num_jobs, job_consumption):\n",
    "    '''Material Waste.\n",
    "    2 points.\n",
    "    This function calculates how much material input will be wasted\n",
    "        after running a certain number of jobs that consume\n",
    "        a set amount of material.\n",
    "    To get the waste of a set of jobs:\n",
    "        1. Multiply the number of jobs by the material consumption per job.\n",
    "        2. Subtract the total material consumed from the total material available.\n",
    "    The users of this function also want you to format the output as a string, annotated with the\n",
    "        units in which the material is expressed. Do not add a space between the number and the unit.\n",
    "    Parameters\n",
    "    ----------\n",
    "    total_material: int\n",
    "        the total material available\n",
    "    material_units: str\n",
    "        the units used to express a quantity of the material (e.g., \"kg\", \"L\", etc.)\n",
    "    num_jobs: int\n",
    "        the number of jobs to run\n",
    "    job_consumption: int\n",
    "        the amount of material consumed per job\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        the amount of remaining material expressed with its unit (e.g., \"10kg\").\n",
    "    '''\n",
    "    # Replace `pass` with your code. \n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    consumption = num_jobs*job_consumption\n",
    "    waste = total_material - consumption\n",
    "    return (f\"{waste}{material_units}\")\n",
    "material_waste(100, \"kg\", 9, 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "61f33a82",
   "metadata": {},
   "outputs": [],
   "source": [
    "def interest(principal, rate, periods):\n",
    "    '''Interest.\n",
    "    3 points.\n",
    "    This function calculates the final value of an investment after\n",
    "        gaining simple interest over a number of periods.\n",
    "    To calculate simple interest, simply multiply the principal to the quantity (rate * time). \n",
    "        Add this amount to the principal to get the final value.\n",
    "    Round down the final amount.\n",
    "    Parameters\n",
    "    ----------\n",
    "    principal: int\n",
    "        the principal (i.e., starting) amount invested, expressed in centavos\n",
    "    rate: float\n",
    "        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)\n",
    "    periods: int\n",
    "        the number of periods invested\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the final value of the investment\n",
    "    '''\n",
    "    # Replace `pass` with your code. \n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    value = (principal+(principal*(rate*periods)))//1\n",
    "    \n",
    "    return value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "111a7ef8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1060.0"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "interest(1000.25,.03,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "2debd833",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25.306173061325712"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def body_mass_index(weight, height):\n",
    "    '''Body Mass Index.\n",
    "    3 points.\n",
    "    This function calculates the body mass index (BMI) of a person\n",
    "        given their weight and height.\n",
    "    The formula for BMI is: kg / (m ^ 2)\n",
    "        (i.e., kilograms over meters squared)\n",
    "    Unfortunately, the users of this function use the imperial system.\n",
    "        You will need to first convert their arguments to the metric system.\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    weight: float\n",
    "        the weight of the person, in pounds\n",
    "    height: list\n",
    "        the height of the person, expressed as a list of two integers.\n",
    "        the first integer is the foot component of their height.\n",
    "        the second integer is the inches component of their height.\n",
    "        for example, 5'10\" would be passed as [5, 10].\n",
    "    Returns\n",
    "    -------\n",
    "    float\n",
    "        the BMI of the person.\n",
    "    '''\n",
    "    # Replace `pass` with your code. \n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    pass\n",
    "    kg = weight/2.2\n",
    "    cm = (height[0] * 30.48) + (height[1] * 2.54 )\n",
    "    BMI = kg/ (cm/100)**2\n",
    "    return(BMI)\n",
    "body_mass_index(176, [5,10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c11c345c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
