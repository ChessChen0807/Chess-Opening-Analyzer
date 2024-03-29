import pandas as pd

# Set pandas display options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Load the dataset from Kaggle
# Dataset download link: https://www.kaggle.com/datasets/datasnaek/chess/data
df = pd.read_csv('games.csv')
df.dropna()


# Get unique opening names
def get_opening_name():
    result = df['opening_name'].unique()
    return result.tolist()


# Get top N opening names by frequency
def get_top_n_opening_name(n):
    # Group the DataFrame by 'opening_name' and get the size (frequency) of each group
    result = df.groupby('opening_name').size()
    # Sort the result by frequency in descending order
    result = result.sort_values(ascending=False).reset_index(name='count')
    return result[:n]


# Get victory status statistics
def get_victory_status():
    # Group the DataFrame by 'opening_name' and 'victory_status' and get the size (count) of each group
    result = df.groupby(['opening_name', 'victory_status']).size()
    # Sort the result by count in descending order
    result = result.sort_values(ascending=False).reset_index(name='count')
    return result


# Get victory status statistics for a specific opening name
def get_victory_status_by_opening_name(opening_name):
    # Filter the DataFrame for rows with a specific 'opening_name'
    # Group the filtered DataFrame by 'opening_name' and 'victory_status' and get the size (count) of each group
    result = df.loc[(df['opening_name'] == opening_name)].groupby(
        ['opening_name', 'victory_status']).size()
    # Sort the result by count in descending order
    result = result.sort_values(ascending=False).reset_index(name='count')
    return result


# Get winner statistics
def get_winner():
    # Group the DataFrame by 'opening_name' and 'winner' and get the size (count) of each group
    result = df.groupby(['opening_name', 'winner']).size()
    # Sort the result by count in descending order
    result = result.sort_values(ascending=False).reset_index(name='count').values.tolist()
    return result


# Get winner statistics for a specific opening name
def get_winner_by_opening_name(opening_name):
    # Filter the DataFrame for rows with a specific 'opening_name'
    # Group the filtered DataFrame by 'opening_name' and 'winner' and get the size (count) of each group
    result = df.loc[(df['opening_name'] == opening_name)].groupby(
        ['opening_name', 'winner']).size()
    # Sort the result by count in descending order
    result = result.sort_values(ascending=False).reset_index(name='count').values.tolist()
    return result


# Get min and max number of moves in the opening phase for a specific opening name
def get_min_max_number_moves_in_the_opening_phase(opening_name):
    # Filter the DataFrame for rows with a specific 'opening_name'
    # Calculate the minimum and maximum values for specified columns ('moves', 'opening_ply') in the filtered DataFrame
    result = df.loc[(df['opening_name'] == opening_name)].agg(['min', 'max'])
    return result[['opening_name', 'victory_status', 'moves', 'opening_ply']]


# Get min and max number of turns for a specific opening name
def get_min_max_number_turns(opening_name):
    # Filter the DataFrame for rows with a specific 'opening_name'
    # Calculate the minimum and maximum values for specified columns ('moves', 'turns') in the filtered DataFrame
    result = df.loc[(df['opening_name'] == opening_name)].agg(['min', 'max'])
    return result[['opening_name', 'victory_status', 'moves', 'turns']]

if __name__ == '__main__':
    # Test get_opening_name function
    opening_names = get_opening_name()
    print("Unique opening names:", opening_names)
    
    # Test get_top_n_opening_name function
    top_n_opening_names = get_top_n_opening_name(5)  # Get top 5 opening names
    print("Top 5 opening names by frequency:")
    print(top_n_opening_names)
    
    # Test get_victory_status function
    victory_status_stats = get_victory_status()
    print("Victory status statistics:")
    print(victory_status_stats.head())
    
    # Test get_victory_status_by_opening_name function
    opening_name = 'Sicilian Defense: Mongoose Variation'
    victory_status_stats_opening = get_victory_status_by_opening_name(opening_name)
    print(f"Victory status statistics for '{opening_name}':")
    print(victory_status_stats_opening)
    
    # Test get_winner function
    winner_stats = get_winner()
    print("Winner statistics:")
    print(winner_stats[:5])  # Print top 5 winners
    
    # Test get_winner_by_opening_name function
    winner_stats_opening = get_winner_by_opening_name(opening_name)
    print(f"Winner statistics for '{opening_name}':")
    print(winner_stats_opening[:5])  # Print top 5 winners for the specified opening name
    
    # Test get_min_max_number_moves_in_the_opening_phase function
    min_max_moves = get_min_max_number_moves_in_the_opening_phase(opening_name)
    print(f"Min and Max number of moves in the opening phase for '{opening_name}':")
    print(min_max_moves)
    
    # Test get_min_max_number_turns function
    min_max_turns = get_min_max_number_turns(opening_name)
    print(f"Min and Max number of turns for '{opening_name}':")
    print(min_max_turns)
