import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv("adult.data.csv")
  print(df.info())

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.

  race_count = df['race'].value_counts()
  #print('RACE_COUNT: ', race_count)

  # What is the average age of men?

  men = df.loc[df['sex'] == "Male", 'age']

  average_age_men = round(men.mean(), 1)
  #print(f"average_age_men:  {average_age_men}")

  # What is the percentage of people who have a Bachelor's degree?
  bachelors = df['education'] == 'Bachelors'
  total_bachelors = df.loc[bachelors].value_counts().sum()
  total_educators = df['education'].value_counts().sum()
  percentage_bachelors = round(total_bachelors * 100 / total_educators, 1)
  print(f"percentage_bachelors: {percentage_bachelors}%")

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?

  # with and without `Bachelors`, `Masters`, or `Doctorate`

  masters = df['education'] == 'Masters'
  doctorates = df['education'] == 'Doctorate'
  
  higher_education = bachelors | masters | doctorates
  

  lower_education = (df['education'] != 'Bachelors') & (
      df['education'] != 'Masters') & (df['education'] != 'Doctorate')


  # percentage with salary >50K
  rich = df['salary'] == '>50K'

  high_edu_rich = df[higher_education & rich].value_counts().sum()

  total_high_edu = df[higher_education].value_counts().sum()

  higher_education_rich = round(high_edu_rich * 100 / total_high_edu, 1)
  #print(f"higher_education_rich: {higher_education_rich}%")

  low_edu_rich = df[lower_education & rich].value_counts().sum()

  total_low_edu = df[lower_education].value_counts().sum()

  lower_education_rich = round(low_edu_rich * 100 / total_low_edu, 1)
  #print(f"lower_education_rich: {lower_education_rich}%")

  # What is the minimum number of hours a person works per week (hours-per-week feature)?

  min_work_hours = df['hours-per-week'].min()
  #print(f"min_work_hours: {min_work_hours} hours per week")

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

  ppl_min_work_hours_rich = df.loc[(df['hours-per-week'] == min_work_hours)
                                   & rich].value_counts().sum()

  num_min_workers = df[df['hours-per-week'] ==
                       min_work_hours].value_counts().sum()

  rich_percentage = round(ppl_min_work_hours_rich * 100 / num_min_workers, 1)

  #print(f"rich_percentage {rich_percentage}%")

  # What country has the highest percentage of people that earn >50K?
  country_rich = df.loc[df['salary'] == '>50K',
                        'native-country'].value_counts()
  country_pop = df['native-country'].value_counts()

  rich_percent_country = round(country_rich * 100 / country_pop, 2)

  #print('Population by country', country_pop)
  #print('Rich by country', country_rich)
  #print('rich percent by country', rich_percent_country)

  highest_earning_country = rich_percent_country.idxmax()
  highest_earning_country_percentage = round(rich_percent_country.max(), 1)

  #print('highest_earning_country:', highest_earning_country)
  #print(f"highest_earning_country_percentage: {highest_earning_country_percentage}%")

  # Identify the most popular occupation for those who earn >50K in India.

  country_rich_occupation = df.loc[(df['native-country'] == 'India') &
                                   (df['salary'] == '>50K'),
                                   'occupation'].value_counts()
  #print('country_rich_occupation:', country_rich_occupation)

  top_IN_occupation = country_rich_occupation.idxmax()
  print('top_IN_occupation:', top_IN_occupation)

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
        f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
        f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
        f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
        f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
      'race_count': race_count,
      'average_age_men': average_age_men,
      'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
      'rich_percentage': rich_percentage,
      'highest_earning_country': highest_earning_country,
      'highest_earning_country_percentage': highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
  }
