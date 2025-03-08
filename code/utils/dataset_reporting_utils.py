import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.text_cleaning_utils import TextCleaner

# Set visualization style
plt.style.use("ggplot")
sns.set_palette("Set2")
plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 12


class DatasetReport:
    """
    A class for analyzing, cleaning, and visualizing text datasets, particularly
    focused on Bangla cyberbullying datasets.
    
    This class provides methods to:
    - Clean datasets using TextCleaner
    - Analyze dataset quality (missing values, duplicates)
    - Visualize class distributions
    - Analyze text length characteristics
    
    Each method generates both console reports and visual plots to facilitate
    comprehensive dataset understanding.
    """

    def clean_dataset(
        self, df: pd.DataFrame, text_column_name: str, dataset_name="Dataset"
    ) -> pd.DataFrame:
        """
        Clean the dataset using TextCleaner and report changes.
        
        Performs sequential cleaning operations including:
        - Removing NA values
        - Converting to string type
        - Removing digits, English characters, special characters 
        - Removing stopwords and emojis
        - Removing empty strings and duplicates
        
        Parameters:
        -----------
        df : pd.DataFrame
            The dataframe containing text data to be cleaned
        text_column_name : str
            The name of the column containing text data
        dataset_name : str, default="Dataset"
            A friendly name for the dataset for reporting purposes
            
        Returns:
        --------
        pd.DataFrame
            A cleaned version of the dataset with problematic records removed
        """
        print(f"\n{'='*20} CLEANING {dataset_name} {'='*20}")

        # Initialize text cleaner
        text_cleaner = TextCleaner()

        # Create a copy for cleaning
        df_cleaned = df.copy()

        # Remove NA values and report
        na_count_before = df_cleaned[text_column_name].isna().sum()
        df_cleaned = df_cleaned.dropna(subset=[text_column_name])
        na_removed = na_count_before - df_cleaned[text_column_name].isna().sum()
        print(f"Removed {na_removed} NA values")

        # Apply text cleaning functions
        print("Applying text cleaning...")
        df_cleaned[text_column_name] = (
            df_cleaned[text_column_name]
            .apply(lambda x: str(x))  # Ensure all values are strings
            .apply(text_cleaner.remove_digits)
            .apply(text_cleaner.remove_english_and_special_chars)
            .apply(text_cleaner.remove_stopwords)
            .apply(text_cleaner.remove_emojis)
        )

        # Check for empty strings after cleaning
        empty_after = df_cleaned[df_cleaned[text_column_name] == ""].shape[0]
        print(f"Empty strings after cleaning: {empty_after}")

        # Remove empty strings
        df_cleaned = df_cleaned[df_cleaned[text_column_name] != ""]
        print(f"Removed {empty_after} empty strings")

        # Check for duplicates after cleaning
        duplicates_after = df_cleaned.duplicated(subset=[text_column_name]).sum()
        print(f"Duplicated texts after cleaning: {duplicates_after}")

        # Remove duplicates
        df_cleaned = df_cleaned.drop_duplicates(subset=[text_column_name])
        print(f"Removed {duplicates_after} duplicates")
        print(f"Final size of cleaned dataset: {len(df_cleaned)}")

        return df_cleaned

    def analyze_dataset_quality(
        self, df: pd.DataFrame, text_column_name: str, dataset_name="Dataset"
    ) -> dict:
        """
        Analyze dataset quality in terms of missing values, empty strings and duplicates.
        
        Generates a comprehensive report on data quality issues including:
        - Count of NA values
        - Count of empty strings
        - Count of duplicate records
        - Top 10 most frequently occurring texts
        
        Parameters:
        -----------
        df : pd.DataFrame
            The dataframe to analyze
        text_column_name : str
            The name of the column containing text data
        dataset_name : str, default="Dataset"
            A friendly name for the dataset for reporting purposes
            
        Returns:
        --------
        dict
            A dictionary containing dataset quality metrics and statistics
        """
        report = {
            "dataset_name": dataset_name,
            "total_records": len(df),
            "na_count": df[text_column_name].isna().sum(),
            "empty_count": (df[text_column_name] == "").sum(),
            "duplicate_count": df.duplicated(subset=[text_column_name]).sum(),
            "top_duplicates": df[text_column_name].value_counts().head(10),
        }

        # Print formatted report
        print(f"\n{'='*20} {dataset_name} QUALITY REPORT {'='*20}")
        print(f"Total records: {report['total_records']}")
        print(
            f"NA values in '{text_column_name}': {report['na_count']} ({report['na_count']/report['total_records']*100:.2f}%)"
        )
        print(
            f"Empty strings: {report['empty_count']} ({report['empty_count']/report['total_records']*100:.2f}%)"
        )
        print(
            f"Duplicate records: {report['duplicate_count']} ({report['duplicate_count']/report['total_records']*100:.2f}%)"
        )

        if report["duplicate_count"] > 0:
            print(f"\nTop 10 most common duplicated texts:")
            for text, count in report["top_duplicates"].items():
                if count > 1:  # Only show duplicates
                    print(f"'{text}': {count} occurrences")

        return report

    @staticmethod
    def analyze_class_distribution(
        df: pd.DataFrame, label_column_name: str, dataset_name="Dataset"
    ):
        """
        Analyze and visualize the class distribution in a dataset.
        
        Generates:
        - Console report of class counts
        - Bar chart visualization of class distribution
        - Pie chart of class percentage breakdown
        
        Parameters:
        -----------
        df : pd.DataFrame
            The dataframe to analyze
        label_column_name : str
            The name of the column containing class labels
        dataset_name : str, default="Dataset"
            A friendly name for the dataset for reporting purposes
            
        Returns:
        --------
        tuple
            (class_counts, class_percentages) - Series containing the count and percentage
            of each class in the dataset
        """
        print(f"\n{'='*20} {dataset_name} CLASS DISTRIBUTION {'='*20}")
        class_counts = df[label_column_name].value_counts()
        print(class_counts)

        # Create visualization for class distribution
        plt.figure(figsize=(10, 6))
        ax = sns.barplot(x=class_counts.index, y=class_counts.values)
        plt.title(f"Class Distribution in {dataset_name}", fontsize=16)
        plt.xlabel("Label", fontsize=14)
        plt.ylabel("Count", fontsize=14)
        plt.xticks(rotation=45)

        # Add count labels on top of bars
        for i, v in enumerate(class_counts.values):
            ax.text(i, v + 0.1, str(v), ha="center", fontsize=12)

        plt.tight_layout()
        plt.show()

        # Calculate class percentages
        class_percentages = class_counts / class_counts.sum() * 100

        # Create pie chart
        plt.figure(figsize=(10, 8))
        plt.pie(
            class_percentages,
            labels=class_percentages.index,
            autopct="%1.1f%%",
            startangle=90,
            textprops={"fontsize": 12},
        )
        plt.title(f"Class Distribution Percentage in {dataset_name}", fontsize=16)
        plt.axis("equal")  # Equal aspect ratio ensures pie is circular
        plt.show()

        return class_counts, class_percentages

    @staticmethod
    def analyze_text_length(
        df: pd.DataFrame,
        text_column_name: str,
        label_column_name: str,
        dataset_name="Dataset",
    ):
        """
        Analyze text length distribution and its relationship with classes.
        
        Generates:
        - Summary statistics of text lengths
        - Histogram of text length distribution with mean and median markers
        - Box plot of text lengths by class
        - Bar chart of average text length by class
        
        Parameters:
        -----------
        df : pd.DataFrame
            The dataframe to analyze
        text_column_name : str
            The name of the column containing text data
        label_column_name : str
            The name of the column containing class labels
        dataset_name : str, default="Dataset"
            A friendly name for the dataset for reporting purposes
            
        Returns:
        --------
        tuple
            (length_stats, avg_length_by_class) - Series containing text length
            statistics and average length by class
        """
        print(f"\n{'='*20} {dataset_name} TEXT LENGTH ANALYSIS {'='*20}")

        # Calculate text lengths
        df["text_length"] = df[text_column_name].apply(len)

        # Show summary statistics
        length_stats = df["text_length"].describe()
        print("Text length statistics:")
        print(length_stats)

        # Create histogram of text lengths
        plt.figure(figsize=(12, 6))
        sns.histplot(df["text_length"], bins=50, kde=True)
        plt.title(f"Distribution of Text Lengths in {dataset_name}", fontsize=16)
        plt.xlabel("Text Length (characters)", fontsize=14)
        plt.ylabel("Frequency", fontsize=14)
        plt.axvline(
            x=length_stats["mean"],
            color="red",
            linestyle="--",
            label=f"Mean: {length_stats['mean']:.1f}",
        )
        plt.axvline(
            x=length_stats["50%"],
            color="green",
            linestyle="--",
            label=f"Median: {length_stats['50%']:.1f}",
        )
        plt.legend()
        plt.show()

        # Distribution of text lengths by class
        plt.figure(figsize=(12, 8))
        sns.boxplot(x=label_column_name, y="text_length", data=df)
        plt.title(f"Text Length Distribution by Class in {dataset_name}", fontsize=16)
        plt.xlabel("Class", fontsize=14)
        plt.ylabel("Text Length (characters)", fontsize=14)
        plt.yscale("log")  # Log scale for better visualization if there are outliers
        plt.xticks(rotation=45)
        plt.show()

        # Average text length by class
        avg_length_by_class = (
            df.groupby(label_column_name)["text_length"]
            .mean()
            .sort_values(ascending=False)
        )
        plt.figure(figsize=(10, 6))
        sns.barplot(x=avg_length_by_class.index, y=avg_length_by_class.values)
        plt.title(f"Average Text Length by Class in {dataset_name}", fontsize=16)
        plt.xlabel("Class", fontsize=14)
        plt.ylabel("Average Length (characters)", fontsize=14)
        plt.xticks(rotation=45)

        # Add average values on top of bars
        for i, v in enumerate(avg_length_by_class):
            plt.text(i, v + 1, f"{v:.1f}", ha="center")

        plt.tight_layout()
        plt.show()

        return length_stats, avg_length_by_class
