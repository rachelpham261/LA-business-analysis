import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

YEAR_TO_USE = 2020

# Load the dataset
file_path = 'location_census_CA.csv'  # Replace with your file path
census_data = pd.read_csv(file_path)
census_data = census_data[census_data['year'] == YEAR_TO_USE]

# Specify the columns to be used for clustering
required_columns = [
    'pop_black', 'pop_asian', 'pop_white_all', 'pop_hispanic', 
    'median_age', 'per_capita_income', 'edu_highschool_percent', 'edu_bachelor_percent'
]

# Check for missing values and fill them with the median if any
if census_data[required_columns].isnull().sum().sum() > 0:
    census_data[required_columns] = census_data[required_columns].fillna(census_data[required_columns].median())

# Normalize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(census_data[required_columns])

# Clustering the data into 6 clusters
kmeans_6 = KMeans(n_clusters=6, init='k-means++', max_iter=300, n_init=10, random_state=0)
census_data['Cluster_6'] = kmeans_6.fit_predict(scaled_data)

# Perform PCA for visualization
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)
pc_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
pc_df['Cluster_6'] = census_data['Cluster_6'].values

# Plotting the clusters using PCA components
plt.figure(figsize=(10, 8))
sns.scatterplot(x="PC1", y="PC2", hue="Cluster_6", palette="Set1", data=pc_df, legend="full")
plt.title('PCA Plot of Census Clusters', fontsize=18)
plt.xlabel('Principal Component 1', fontsize=15)
plt.ylabel('Principal Component 2', fontsize=15)
# change font size of legend, code below
legend = plt.legend()
plt.setp(legend.get_texts(), fontsize='12')
plt.savefig('pca_plot.png', bbox_inches='tight')
plt.close()

# Saving clusters to different CSV files
output_columns = ['GEOID'] + required_columns + ['Cluster_6']
for cluster_id in range(6):
    cluster_data = census_data[census_data['Cluster_6'] == cluster_id]
    cluster_data.to_csv(f'cluster_{cluster_id}.csv', index=False, columns=output_columns)