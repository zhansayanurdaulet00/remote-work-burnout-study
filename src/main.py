import os
import yaml
import pandas as pd
import statsmodels.api as sm

def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    sample_path = config["data"]["sample_path"]
    log_path = config["data"]["output_log_path"]
    
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    df = pd.read_csv(sample_path)
    
    X_vars = config["variables"]["independent"] + config["variables"]["controls"]
    X = sm.add_constant(df[X_vars])
    y = df[config["variables"]["dependent"]]
    
    model = sm.OLS(y, X).fit()
    
    with open(log_path, "w") as log_file:
        log_file.write("=== BENCHMARK EXECUTION LOG ===\n")
        log_file.write(f"Processed rows: {len(df)}\n\n")
        log_file.write(str(model.summary()))
        log_file.write("\n\nPipeline execution status: SUCCESS\n")
    
    print(f"Benchmark completed successfully! Logs saved to {log_path}")

if __name__ == "__main__":
    main()
