# Data Orchestration with Mage.ai
Build data pipelines for staging process with data orchestration Mage.ai, insert data into Postgres Database and Google Cloud Storage.

### Dataset
Source: https://data.mendeley.com/datasets/8gx2fvg2k6/5

URL = https://data.mendeley.com/public-files/datasets/8gx2fvg2k6/files/72784be5-36d3-44fe-b75d-0edbf1999f65/file_downloaded

Downloading the data
```bash
wget https://github.com/trquanganhng/DataCoSupplyChain/releases/download/Download/DataCoSupplyChainDataset.csv
```

### Description
Using orchestration Mage.ai, I created 2 pipelines to process the dataset separating them into different tables and inserting into Postgres Database and Google Cloud Storage.

## Usage
#### MacOS

#### Clone Repository
```bash
git clone https://github.com/trquanganhng/mage-datacosupplychain.git
```

#### Build the container
Navigate to the repo and build the container

```bash
docker compose build
```

#### Run the container
```bash
docker compose up
```
Now, navigate to http://localhost:6789 in your browser


