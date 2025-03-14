# Data Visualization
# 1 Teams with Most Wins (Bar Chart)

plt.figure(figsize=(10,5))
sns.barplot(x=team_wins.index, y=team_wins.values, palette="coolwarm")
plt.xlabel("Teams")
plt.ylabel("Total Wins")
plt.title("IPL 2024 - Team Wins")
plt.xticks(rotation=45)
plt.show() 

# 2 Most Runs by a Player (Top 5)

top_scorers = df.groupby("most_runs")["most_runs"].count().sort_values(ascending=False).head(5)
plt.figure(figsize=(10,5))
sns.barplot(x=top_scorers.index, y=top_scorers.values, palette="magma")
plt.xlabel("Players")
plt.ylabel("Number of Matches Top Scorer")
plt.title("Top 5 Run Scorers - IPL 2024")
plt.xticks(rotation=45)
plt.show()

# 3 Impact of Toss Decision on First Innings Score

plt.figure(figsize=(8,5))
sns.boxplot(x=df["decision"], y=df["first_score"], palette="viridis")
plt.xlabel("Toss Decision")
plt.ylabel("First Innings Score")
plt.title("Impact of Toss Decision on First Innings Score")
plt.show()

# 4 Predicting Match Winner (Simple Machine Learning)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
# Encode categorical columns
le = LabelEncoder()
df_encoded = df.copy()
for col in ["team1", "team2", "toss_winner", "decision", "winner"]:
    df_encoded[col] = le.fit_transform(df[col])
# Prepare data
X = df_encoded[["team1", "team2", "toss_winner", "decision"]]  # Features
y = df_encoded["winner"]  # Target
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
# Model accuracy
accuracy = model.score(X_test, y_test)
print(f"Prediction Accuracy: {accuracy * 100:.2f}%")