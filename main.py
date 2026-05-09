import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

# -----------------------------------
# LOAD DATA
# -----------------------------------

campaigns_df = pd.read_csv(
    "datasets/campaigns.csv"
)

# -----------------------------------
# ENCODERS
# -----------------------------------

platform_encoder = LabelEncoder()

campaigns_df["platform_encoded"] = (
    platform_encoder.fit_transform(
        campaigns_df["platform"]
    )
)

# -----------------------------------
# GENERATED BUDGET COLUMN
# -----------------------------------

campaigns_df["budget"] = (
    campaigns_df["impressions"] * 4
)

# -----------------------------------
# FEATURES
# -----------------------------------

X = campaigns_df[
    [
        "budget",
        "impressions",
        "clicks",
        "engagement_rate",
        "platform_encoded"
    ]
]

y = campaigns_df["roi_percentage"]

# -----------------------------------
# TRAIN TEST SPLIT
# -----------------------------------

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
)

# -----------------------------------
# MODEL
# -----------------------------------

model = LinearRegression()

model.fit(X_train, y_train)

# -----------------------------------
# ACCURACY
# -----------------------------------

predictions = model.predict(X_test)

accuracy = abs(
    r2_score(
        y_test,
        predictions
    )
)

# -----------------------------------
# PREDICTION FUNCTION
# -----------------------------------

def predict_roi(
    budget,
    impressions,
    clicks,
    engagement_rate,
    platform
):

    platform_value = (
        platform_encoder.transform(
            [platform]
        )[0]
    )

    prediction = model.predict([
        [
            budget,
            impressions,
            clicks,
            engagement_rate,
            platform_value
        ]
    ])

    return prediction[0]

