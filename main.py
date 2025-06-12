import pandas as pd
from scipy.stats import ttest_ind, norm
import matplotlib.pyplot as plt
import numpy as np

df_test = pd.read_csv('./test_group.csv', sep=';')
df_control = pd.read_csv(f'./control_group.csv', sep=';')

# Обчислення CTR
df_test = df_test[df_test['# of Impressions'] > 0].copy()
df_control = df_control[df_control['# of Impressions'] > 0].copy()

df_test['CTR'] = df_test['# of Website Clicks'] / df_test['# of Impressions']
df_control['CTR'] = df_control['# of Website Clicks'] / df_control['# of Impressions']

# Статистичний тест
t_stat, p_value = ttest_ind(df_test['CTR'], df_control['CTR'], equal_var=False)

print("Результати t-тесту для CTR:")
print(f"t-статистика: {t_stat:.4f}")
print(f"p-значення: {p_value:.4f}")

if p_value < 0.05:
    print("Результат є статистично значущим: CTR у групах різниться.")
else:
    print("Немає статистично значущої різниці між CTR у групах.")

# Column rename
df_test.columns = df_test.columns.str.strip()
df_control.columns = df_control.columns.str.strip()

# Сумарні значення по етапах воронки
steps = [
    '# of Impressions',
    '# of Website Clicks',
    '# of Searches',
    '# of View Content',
    '# of Add to Cart',
    '# of Purchase'
]

test_totals = df_test[steps].sum()
control_totals = df_control[steps].sum()

# Побудова воронки
plt.figure(figsize=(10, 6))
plt.plot(steps, test_totals, marker='o', label='Test Campaign')
plt.plot(steps, control_totals, marker='o', label='Control Campaign')
plt.xticks(rotation=45)
plt.title("Проходження воронки: Test vs Control")
plt.xlabel("Етап воронки")
plt.ylabel("Кількість користувачів")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Видаляємо можливі пропуски в потрібних колонках
df_control = df_control.dropna(subset=["# of Add to Cart", "# of Purchase"])
df_test = df_test.dropna(subset=["# of Add to Cart", "# of Purchase"])

# Підрахунок загальної кількості доданих до кошика та покупок
control_cart = df_control["# of Add to Cart"].sum()
control_purchase = df_control["# of Purchase"].sum()

test_cart = df_test["# of Add to Cart"].sum()
test_purchase = df_test["# of Purchase"].sum()

# Конверсії
control_cr = control_purchase / control_cart
test_cr = test_purchase / test_cart

# Різниця конверсій
diff = test_cr - control_cr

# Стандартна похибка різниці конверсій
se = np.sqrt((control_cr * (1 - control_cr)) / control_cart + 
             (test_cr * (1 - test_cr)) / test_cart)

# 95% довірчий інтервал
z_score = norm.ppf(0.975)
ci_lower = diff - z_score * se
ci_upper = diff + z_score * se

# Вивід результатів
print(f"Control conversion: {control_cr:.2%}")
print(f"Test conversion: {test_cr:.2%}")
print(f"Difference in conversion: {diff:.2%}")
print(f"95% Confidence Interval: [{ci_lower:.2%}, {ci_upper:.2%}]")