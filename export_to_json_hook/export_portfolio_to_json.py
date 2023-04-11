from pathlib import Path

from data_portfolio import Portfolio

if __name__ == "__main__":
    # Create a portfolio object
    portfolio = Portfolio()

    # Path to the datasets list
    path_to_datasets = Path(__file__).parent.parent / "datasets" / "datasets.json"

    # Export the portfolio to json
    portfolio.to_json(path_to_datasets)
