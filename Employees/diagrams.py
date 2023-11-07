import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_csv_file(file_path):
    try:
        data = pd.read_csv('employees.csv', encoding='utf-8')
        return data
    except FileNotFoundError:
        print("Помилка: Файл CSV не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}. Неможливо відкрити файл CSV.")
        return None


def calculate_age(birth_date):
    birth_date = pd.to_datetime(birth_date)
    today = pd.to_datetime('today')
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def count_gender(data):
    gender_counts = data['Стать'].value_counts()
    return gender_counts


def count_age_categories(data):
    bins = [0, 18, 45, 70, 100]
    age_labels = ["до 18", "18-45", "45-70", "старше 70"]
    data['Вік'] = data['Дата народження'].apply(calculate_age)
    data['Вікова категорія'] = pd.cut(data['Вік'], bins=bins, labels=age_labels)
    age_category_counts = data['Вікова категорія'].value_counts()
    return age_category_counts


def count_gender_age_categories(data):
    gender_age_counts = data.groupby(['Вікова категорія', 'Стать']).size().unstack(fill_value=0)
    return gender_age_counts


def main():
    data = read_csv_file('empoyees.csv')
    if data is not None:
        print("Ok: Файл CSV успішно завантажено.")

        # Рахуємо кількість співробітників чоловічої та жіночої статі
        gender_counts = count_gender(data)
        print("\nКількість співробітників за статтю:")
        print(gender_counts)

        # Рахуємо кількість співробітників кожної вікової категорії
        age_category_counts = count_age_categories(data)
        print("\nКількість співробітників в різних вікових категоріях:")
        print(age_category_counts)

        # Рахуємо кількість співробітників жіночої та чоловічої статі кожної вікової категорії
        gender_age_counts = count_gender_age_categories(data)
        print("\nКількість співробітників чоловічої та жіночої статі в різних вікових категоріях:")
        print(gender_age_counts)

        # Побудова діаграми для розподілу статей
        plt.figure(figsize=(8, 6))
        sns.barplot(x=gender_counts.index, y=gender_counts.values)
        plt.title("Розподіл співробітників за статтю")
        plt.xlabel("Стать")
        plt.ylabel("Кількість")
        plt.show()

        # Побудова діаграми для розподілу вікових категорій
        plt.figure(figsize=(8, 6))
        sns.barplot(x=age_category_counts.index, y=age_category_counts.values)
        plt.title("Розподіл співробітників за віковими категоріями")
        plt.xlabel("Вікова категорія")
        plt.ylabel("Кількість")
        plt.show()

        # Побудова діаграм для розподілу статей та вікових категорій
        fig, axes = plt.subplots(2, 2, figsize=(10, 10))
        colors = ['lightblue', 'lightcoral']

        for i, age_category in enumerate(gender_age_counts.index):
            ax = axes[i // 2, i % 2]
            ax.pie(gender_age_counts.loc[age_category], labels=gender_age_counts.columns, colors=colors,
                   autopct='%1.1f%%', startangle=140, pctdistance=0.85)
            ax.set_title(f"Вікова категорія: {age_category}")

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
