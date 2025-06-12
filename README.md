# 📊 A/B Testing Project: Evaluating a New Online Advertising Strategy

## 📁 Project Overview

This project simulates and analyzes the results of an A/B test to evaluate the effectiveness of a new online advertising approach. The goal is to determine whether the new strategy leads to improved user engagement and conversions compared to the traditional one.

---

## 🎯 Objectives

* Assess if the new advertising approach improves:

  * Click-through rate (CTR)
  * Conversion rate (CR)
  * Return on Ad Spend (ROAS)
* Identify potential drop-off points in the user journey.
* Provide data-driven recommendations based on the funnel performance.

---

## 🧪 A/B Test Design

* **Control Group**: Shown the standard ads.
* **Test Group**: Shown ads using a new approach.
* **Split**: 50% control / 50% test
* **Metrics Measured**:

  * CTR, CPC, CPA, CR, ROAS

---

## 📌 Tracking Plan

Tracked user behavior at each interaction stage:

| Event           | Description         | Key Attributes                    |
| --------------- | ------------------- | --------------------------------- |
| `ad_impression` | Ad shown to user    | campaign\_name, date, user\_id    |
| `ad_click`      | Click on ad         | campaign\_name, ad\_id, user\_id  |
| `search`        | Site search         | search\_term, timestamp, user\_id |
| `view_content`  | Product view        | product\_id, price, category      |
| `add_to_cart`   | Add product to cart | product\_id, price, quantity      |
| `purchase`      | Purchase made       | order\_id, total\_value, items    |

---

## 📊 Analysis Summary

### ✅ Task 3 – Statistical Significance

* Used Welch’s t-test to compare CTR.
* **p-value**: `0.0003` → **Statistically significant** difference.
* **Conclusion**: Test group significantly outperformed control on CTR.

### 📉 Task 4 – Funnel Visualization

Visualized drop-off through stages:

* 🚀 Test campaign outperforms control in **clicks, searches, views**.
* ⚠️ Drop-off after "add to cart" is almost equal across groups.
* ✅ Final **conversion rate** is **45% higher** in the test group.

### 📐 Task 5 – Confidence Interval for Purchase Conversion

Compared conversions from `add_to_cart → purchase`:

* **Control CR**: `40.21%`
* **Test CR**: `59.13%`
* **Difference**: `+18.91%`
* **95% CI**: `[+18.14%, +19.69%]` → Statistically significant improvement.

---

## 📈 Key Conclusions

* The new ad strategy significantly boosts user engagement and final purchases.
* Conversion from add-to-cart is also meaningfully higher in the test group.
* Opportunity: Analyze why add-to-cart rate didn't increase as much as upstream steps.

---

## 🛠️ Technologies Used

* **Python** (Pandas, NumPy, SciPy, Matplotlib)
* **A/B Testing Statistics**
* **Funnel Visualization**
* **Confidence Intervals & t-tests**

---

## ✅ Recommendations

* **Adopt the new ad approach** based on higher CTR and CR.
* **Investigate cart UI/UX** to address plateau in add-to-cart behavior.
* **Continue monitoring** long-term trends for retention and ROAS.

