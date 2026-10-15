
import os
import yaml
import pandas as pd


def main():
    # 1. Load configuration
    with open("config.yaml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    sample_path = config["data"]["sample_path"]
    log_path = config["data"]["output_log_path"]

    # 2. Check input file
    if not os.path.exists(sample_path):
        raise FileNotFoundError(
            f"Sample dataset not found: {sample_path}"
        )

    # 3. Read sample dataset
    df = pd.read_csv(sample_path)

    # 4. Validate required columns
    variables = config["variables"]

    required_columns = (
        variables["independent"]
        + [variables["dependent"]]
        + variables["moderators"]
        + variables["controls"]
    )

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if df.empty:
        raise ValueError("The dataset is empty.")

    # 5. Calculate descriptive statistics
    numeric_columns = list(dict.fromkeys(required_columns))
    numeric_data = df[numeric_columns].apply(
        pd.to_numeric, errors="coerce"
    )

    if numeric_data.isna().any().any():
        raise ValueError(
            "Missing or non-numeric values found "
            "in required analysis columns."
        )

    summary = numeric_data.describe().round(3)

    # 6. Save the test log
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    with open(log_path, "w", encoding="utf-8") as log_file:
        log_file.write("=== RESEARCH PIPELINE TEST LOG ===\n")
        log_file.write(f"Processed rows: {len(df)}\n")
        log_file.write(
            "Purpose: pipeline smoke test, not "
            "scientific hypothesis testing.\n\n"
        )
        log_file.write("=== DESCRIPTIVE STATISTICS ===\n")
        log_file.write(summary.to_string())
        log_file.write("\n\nPipeline execution status: SUCCESS\n")

    print("Pipeline test completed successfully!")
    print(f"Processed rows: {len(df)}")
    print(f"Log saved to: {log_path}")


if __name__ == "__main__":
    main()
