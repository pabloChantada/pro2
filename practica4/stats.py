import pandas as pd

class Statistics:
    def avl_to_list(tree):
        data = []
        # Assuming 'tree' can be directly iterated to yield Curso objects
        for i in tree:
            # Convert each Curso object into a dictionary
            data.append([
                tree[i].name,
                tree[i].duration,
                tree[i].students,
                tree[i].level,
                tree[i].language,
                tree[i].price,
            ])
        return data
    
    def mean_language(tree):
        formatted_data = Statistics.avl_to_list(tree)
        # Create DataFrame with appropriate column names
        df = pd.DataFrame(formatted_data, columns=['name', 'duration', 'students', 'level', 'language', 'price'])
        result = df.groupby('language')['students'].agg(['mean', 'std']).round(2).fillna(0)
        print(result)
        return result

    def mean_level(tree):
        formatted_data = Statistics.avl_to_list(tree)
        # Create DataFrame with appropriate column names
        df = pd.DataFrame(formatted_data, columns=['name', 'duration', 'students', 'level', 'language', 'price'])
        result = df.groupby('level')['students'].agg(['mean', 'std']).round(2).fillna(0)
        print(result)
        return result

    
    def total_income(tree):
        formatted_data = Statistics.avl_to_list(tree)
        # Create DataFrame with appropriate column names
        df = pd.DataFrame(formatted_data, columns=['name', 'duration', 'students', 'level', 'language', 'price'])
        df['total_income'] = df['price'] * df['students'] * df['duration']
        total_revenue = df['total_income'].sum()
        print(f"Total revenue: {total_revenue}")
        return total_revenue

    