from pathlib import Path

from microscopy_portfolio import Portfolio

if __name__ == "__main__":
    # Create a portfolio object
    portfolio = Portfolio()

    # Path to the datasets list
    path_to_datasets = Path(".", "datasets", "registry.txt")

    # Export the portfolio to json
    portfolio.to_registry(path_to_datasets)
