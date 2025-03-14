# Exploratory Data Analysis (EDA)
# 1 Most Successful Teams (Highest Wins)

# Count number of matches won by each team
team_wins = df["winner"].value_counts()
# Display top teams
print(team_wins)

# 2 Toss Impact on Match Results

# Count number of times toss winner won the match
toss_impact = (df["toss_winner"] == df["winner"]).sum()
# Print results
print(f"Toss winner also won the match in {toss_impact} out of {len(df)} matches ({(toss_impact / len(df)) * 100:.2f}%)")

# 3 Best Players (Most Player of the Match Awards)

# Count Player of the Match frequency
best_players = df["player_of_the_match"].value_counts().head(5)
# Display results
print(best_players)