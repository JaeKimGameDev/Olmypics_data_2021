import pandas as pd
import csv
import plotly.express as px

DATA_FILE_PATH = r'C:\Users\Jae\Documents\GitHub\Olmypics_data_2021\athlete_Dataset.csv'
OUTPUT_PATHS = {
    'gender': 'AthleteDataByGender.csv',
    'weight': 'AthleteDataByWeight.csv',
    'height': 'AthleteDataByHeight.csv'
}
PARIS_SPORTS = [
    'Archery', 'Gymnastics', 'Athletics', 'Badminton', 'Basketball', 'Beach Volleyball', 'Boxing', 'Diving', 'Fencing',
    'Football', 'Golf', 'Handball', 'Hockey', 'Judo', 'Modern Pentathlon', 'Rhythmic Gymnastics', 'Rowing',
    'Rugby Sevens', 'Sailing', 'Shooting', 'Swimming', 'Table Tennis', 'Taekwondo', 'Tennis', 'Triathlon',
    'Volleyball', 'Water Polo', 'Weightlifting', 'Wrestling'
]
MEDAL_TYPES = ['Gold', 'Silver', 'Bronze']

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data.query("Medal.notnull() & Season == 'Summer' & Year >= 1990")
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def write_csv(file_path, fields, rows):

    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerows(rows)
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")

    return


def generate_grouped_data(data, group_by, ranges, output_file):
    for gender in ['M', 'F']:
        for sport in data['Sport'].unique():
            for medal in ['Gold', 'Silver', 'Bronze']:
                for condition in ranges:
                    if '-' in condition:
                        lower, upper = condition.strip("()").split('-')
                        query_condition = f"{group_by} >= {lower} & {group_by} <= {upper}"
                    elif '>' in condition or '<' in condition:
                        query_condition = f"{group_by} {condition}"
                    else:
                        print(f"Invalid range condition: {condition}")
                        continue

                    query_string = (
                        f"{query_condition} & Sex == '{gender}' & Sport == '{sport}' & Medal == '{medal}'"
                    )

    return


def DrawBargraphByHeight(data, sport_name, height_ranges, gender):
    sport_data = data[(data['Sport'] == sport_name) & (data['Sex'] == gender)]

    medal_counts = []
    for medal in ['Gold', 'Silver', 'Bronze']:
        for condition in height_ranges:
            if '-' in condition:
                lower, upper = condition.strip("()").split('-')
                query_condition = f"Height >= {lower} & Height <= {upper}"
            elif '>' in condition or '<' in condition:
                query_condition = f"Height {condition}"
            else:
                continue

            query_string = f"{query_condition} & Medal == '{medal}'"
            try:
                result = sport_data.query(query_string)
                count = len(result)
                medal_counts.append({
                    'Height Range': condition,
                    'Medal': medal,
                    'Count': count
                })
            except Exception as e:
                print(f"Failed to execute query: {query_string}")
                print(f"Error: {e}")

    medal_df = pd.DataFrame(medal_counts)

    fig = px.bar(
        medal_df,
        x="Height Range",
        y="Count",
        color="Medal",
        color_discrete_map={
            'Gold': 'gold',
            'Silver': 'silver',
            'Bronze': '#cd7f32'
        },
        title=f"Medal Distribution in {sport_name} ({gender}) by Height Range",
        labels={"Height Range": "Height Range (cm)", "Count": "Medal Count"},
        text="Count",
        barmode="group",
    )
    fig.update_layout(
        xaxis=dict(title="Height Range (cm)"),
        yaxis=dict(title="Medal Count"),
        template="plotly_white"
    )
    fig.show()

    return


def DrawBargraphByAge(data, sport_name, age_ranges, gender):
    sport_data = data[(data['Sport'] == sport_name) & (data['Sex'] == gender)]

    medal_counts = []
    for medal in ['Gold', 'Silver', 'Bronze']:
        for condition in age_ranges:
            if '-' in condition:
                lower, upper = condition.strip("()").split('-')
                query_condition = f"Age >= {lower} & Age <= {upper}"
            elif '>' in condition or '<' in condition:
                query_condition = f"Age {condition}"
            else:
                continue

            query_string = f"{query_condition} & Medal == '{medal}'"
            try:
                result = sport_data.query(query_string)
                count = len(result)
                medal_counts.append({
                    'Age Range': condition,
                    'Medal': medal,
                    'Count': count
                })
            except Exception as e:
                print(f"Failed to execute query: {query_string}")
                print(f"Error: {e}")

    medal_df = pd.DataFrame(medal_counts)

    fig = px.bar(
        medal_df,
        x="Age Range",
        y="Count",
        color="Medal",
        color_discrete_map={
            'Gold': 'gold',
            'Silver': 'silver',
            'Bronze': '#cd7f32'
        },
        title=f"Medal Distribution in {sport_name} ({gender}) by Age Range",
        labels={"Age Range": "Age Range", "Count": "Medal Count"},
        text="Count",
        barmode="group",
    )
    fig.update_layout(
        xaxis=dict(title="Age Range"),
        yaxis=dict(title="Medal Count"),
        template="plotly_white"
    )
    fig.show()

    return


def DrawBarGraphBySport(file_path, group_by, gender):
    df = pd.read_csv(file_path)
    df = df[df['Gender'] == gender.upper()]

    fig = px.histogram(
        df,
        x="Sport",
        y=list(df.columns[2:-1]),
        barmode='group',
        title=f"Number of Athletes by {group_by} and Gender ({gender.upper()})",
        labels={"x": "Sports", "y": "Number of Athletes"}
    )
    fig.update_layout(legend_title=f"{group_by} Groups")
    fig.show()

    return


def main():
    athlete_data = load_data(DATA_FILE_PATH)
    if athlete_data is None:
        return

    age_ranges = {
        '<21': '< 21', '(21-25)': '>= 21 & Age < 26', '(26-30)': '>= 26 & Age < 31', '>30': '>= 30'
    }
    height_ranges = {
        '<160': '< 160', '(160-170)': '>= 160 & Height <= 170', '(171-180)': '> 170 & Height <= 180', '(181-190)': '> 180 & Height <= 190', '>190': '> 190'
    }
    weight_ranges = {
        '<60': '< 60', '(60-70)': '>= 60 & Weight <= 70', '(71-80)': '> 70 & Weight <= 80', '(81-90)': '> 80 & Weight <= 90', '>91': '> 90'
    }

    generate_grouped_data(athlete_data, 'Age', age_ranges, OUTPUT_PATHS['gender'])
    DrawBarGraphBySport(OUTPUT_PATHS['gender'], 'Age', 'M')
    DrawBarGraphBySport(OUTPUT_PATHS['gender'], 'Age', 'F')

    generate_grouped_data(athlete_data, 'Weight', weight_ranges, OUTPUT_PATHS['weight'])
    DrawBarGraphBySport(OUTPUT_PATHS['weight'], 'Weight', 'M')
    DrawBarGraphBySport(OUTPUT_PATHS['weight'], 'Weight', 'F')

    generate_grouped_data(athlete_data, 'Height', height_ranges, OUTPUT_PATHS['height'])
    DrawBarGraphBySport(OUTPUT_PATHS['height'], 'Height', 'M')
    DrawBarGraphBySport(OUTPUT_PATHS['height'], 'Height', 'F')

    DrawBargraphByHeight(athlete_data, 'Swimming', height_ranges, 'M')
    DrawBargraphByHeight(athlete_data, 'Swimming', height_ranges, 'F')

    DrawBargraphByHeight(athlete_data, 'Basketball', height_ranges, 'M')
    DrawBargraphByHeight(athlete_data, 'Basketball', height_ranges, 'F')

    DrawBargraphByAge(athlete_data, 'Swimming', age_ranges, 'M')
    DrawBargraphByAge(athlete_data, 'Swimming', age_ranges, 'F')
    DrawBargraphByAge(athlete_data, 'Basketball', age_ranges, 'M')
    DrawBargraphByAge(athlete_data, 'Basketball', age_ranges, 'F')

if __name__ == "__main__":
    main()
