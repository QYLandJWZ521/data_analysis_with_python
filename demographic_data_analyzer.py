import pandas as pd

def calculate_demographic_data():
    df = pd.read_csv('adult.data', header=None, names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'])

    race_count = df['race'].value_counts()

    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df.loc[higher_education, 'salary'] == '>50K').mean() * 100, 1)

    lower_education = ~higher_education
    lower_education_rich = round((df.loc[lower_education, 'salary'] == '>50K').mean() * 100, 1)

    min_work_hours = df['hours-per-week'].min()

    min_workers = df['hours-per-week'] == min_work_hours
    rich_percentage_min_workers = round((df.loc[min_workers, 'salary'] == '>50K').mean() * 100, 1)

    country_counts = df['native-country'].value_counts()
    country_rich_counts = df.loc[df['salary'] == '>50K', 'native-country'].value_counts()
    rich_percentage_by_country = (country_rich_counts / country_counts).fillna(0)
    highest_earning_country = rich_percentage_by_country.idxmax()
    highest_earning_country_percentage = round(rich_percentage_by_country.max() * 100, 1)

    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_workers': rich_percentage_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
