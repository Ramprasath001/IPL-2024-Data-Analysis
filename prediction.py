# Count number of matches won by each team
team_wins = df["winner"].value_counts().reset_index()
team_wins.columns = ["team", "wins"]
# Sort by wins
team_wins = team_wins.sort_values(by="wins", ascending=False)
# Display data
print(team_wins)
plt.figure(figsize=(10,5))
# Line plot
sns.lineplot(x=team_wins["team"], y=team_wins["wins"], marker="o", linestyle="-", color="b")
# Labels and title
plt.xlabel("Teams")
plt.ylabel("Total Wins in IPL 2024")
plt.title("Trend Analysis - Which Team Can Win IPL 2025?")
plt.xticks(rotation=45)
plt.grid(True)
# Show plot
plt.show()
