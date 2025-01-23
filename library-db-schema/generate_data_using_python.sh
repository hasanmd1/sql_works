#!/bin/bash

# Generate sample data use python3 or higher
python -m pip install faker && python generate_sample_data.py
echo "Sample data has been generated"

# Load sample data into MySQL
# we are skipping as user may not have MySQL/PostgreSQL installed