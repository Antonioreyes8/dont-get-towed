# !/bin/bash

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Create directories
mkdir -p lambda_package

# Install dependencies
pip install -r requirements.txt -t lambda_package/

# Copy lambda function
cp lambda_function.py lambda_package/

# Create deployment package
cd lambda_package
zip -r ../deployment_package.zip .
cd ..

# Clean up
rm -rf lambda_package
deactivate
rm -rf venv

echo "Deployment package created: deployment_package.zip"