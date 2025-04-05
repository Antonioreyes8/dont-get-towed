# Parking Permit Renewal Automation with AWS

## What's Going On Here? (ELI5)

Imagine you have a robot (AWS Lambda) that needs to fill out a form every day to keep your car from getting towed. This robot lives in Amazon's computer cloud (AWS). We give the robot special tools (Selenium and Chrome) to use a web browser, just like you would. Every day at the same time, an alarm clock (EventBridge) wakes up the robot to do its job. We pack all the robot's instructions (Python code) and tools into neat packages (ZIP files) and use a special delivery service (SAM - Serverless Application Model) to send everything to Amazon's cloud. SAM is like a moving company that knows exactly where to put all your robot's stuff in its new AWS home.

## AWS Tools We're Using

- AWS Lambda: A service that runs your code without needing a full computer. It's like having a robot that wakes up, does one job, then goes back to sleep - you only pay for when it's awake.

- Amazon EventBridge: Works like an alarm clock, telling Lambda when to run your code (in this case, once a day).

- AWS SAM (Serverless Application Model): A tool that helps set up your AWS resources. It reads a recipe (template.yaml) and creates everything you need automatically.

- AWS Layers: A way to share common tools (like Chrome and Selenium) between different Lambda functions. Think of it like a toolbox that multiple robots can share.

## AWS Lambda Parking Permit Renewal Automation

This project automates the daily renewal of parking permits using AWS Lambda with Selenium for web automation. The system runs once per day to ensure the parking permit stays active.

## Project Structure

```md
aws_lambda/
├── .aws-sam/ # SAM deployment artifacts (do not commit to version control)
├── prezip/ # Directory for pre-zipped files
├── lambda_function.py # Main Lambda function code
├── template.yaml # SAM template for AWS infrastructure
├── samconfig.toml # SAM configuration file
├── requirement.txt # Python dependencies
├── build.sh # Build script for deployment package
├── deployment_package.zip # Packaged Lambda function
└── selenium_layer.zip # Selenium and Chrome dependencies
```

## Key Components

### 1. `lambda_function.py`

The main function that automates parking permit renewal. Basically the same code that is the `dont-tow-antonio.py`, just wrapped in a special AWS function.

**Key Features:**

- Uses Selenium WebDriver with headless Chrome (headless chrome is chrome, but since AWS Lambda is serverless and doesn't use a computer screen it is the "headless version" runs on code and commands)
- Automates form filling on apartmentpermits.com
- Includes error handling and logging
- Returns JSON responses for success/failure

**Main Functions in `lambda_function.py`:**

```python
def get_chrome_options():
    # Configures Chrome options for headless operation in Lambda
    # Returns: Chrome options object with Lambda-compatible settings

def lambda_handler(event, context):
    # Main entry point for Lambda execution
    # Parameters:
    #   event: AWS Lambda event object
    #   context: AWS Lambda context object
    # Returns: JSON response with status and message
```

### 2. `template.yaml`

SAM template defining AWS infrastructure.

**Key Resources:**

- Lambda Function Configuration
- Event Schedule (daily trigger)
- IAM Roles and Permissions (these are AWS settings that allows certain accounts to run certain services, like lambda functions)
- Selenium Layer Configuration (this contains the selenium packages as well as chrome)

### 3. `build.sh`

Build script for creating the deployment package.

**Functions:**

1. Creates virtual environment
2. Installs dependencies
3. Packages function code
4. Creates deployment ZIP
5. Cleans up temporary files

### 4. `requirement.txt`

Python dependencies including:

- selenium
- webdriver-manager
- Other supporting packages

### 5. Deployment Packages

- `deployment_package.zip` (15MB): Contains Lambda function and dependencies
- `selenium_layer.zip` (139MB): Contains Chrome and Selenium binaries
  - Note that we may just use the public package provided by AWS since our zip size is too big.

## Setup and Deployment

### Prerequisites

1. AWS CLI installed and configured (https://aws.amazon.com/cli/)
   1. Run `aws configure` to set up after installing AWS
2. SAM CLI installed (https://github.com/aws/aws-sam-cli/releases)
3. Python 3.9
4. Proper AWS credentials (https://www.youtube.com/watch?v=ne8LrbCzW0Q) (https://www.youtube.com/watch?v=ubrE4xq9_9c)

### Deployment Steps

1. **Build the Project:**

   ```bash
   ./build.sh
   ```

2. **Deploy using SAM:**

   ```bash
   sam build
   sam deploy --guided
   ```

3. **First-time Configuration:**
   - Stack Name: Choose a name (e.g., `parking-permit-stack`)
   - AWS Region: Your preferred region
   - Confirm changes before deployment: Yes
   - Allow SAM CLI IAM role creation: Yes

### Configuration

The Lambda function is configured to run:

- Runtime: Python 3.9
- Memory: 512MB
- Timeout: 300 seconds (5 minutes)
- Schedule: Daily at 12:00 UTC

## Troubleshooting

### Common Issues

1. **Selenium Layer Size:**

   - If layer is too large (>250MB), use public layer:

   ```yaml
   Layers:
     - arn:aws:lambda:us-east-1:764866452798:layer:chrome-selenium:31
   ```

2. **Timeout Issues:**

   - Check network connectivity
   - Verify website responsiveness
   - Review Lambda timeout settings

3. **Permission Issues:**
   - Verify IAM roles
   - Check Lambda execution role
   - Ensure EventBridge permissions

### Logging

- CloudWatch Logs contain detailed execution logs
- Success/failure status in Lambda response
- Error messages include stack traces

## Best Practices

1. **Version Control:**

   - Don't commit `.aws-sam/`
   - Don't commit ZIP files
   - Use `.gitignore`

2. **Security:**

   - Keep credentials secure
   - Use environment variables
   - Regular security updates

3. **Maintenance:**
   - Monitor execution logs
   - Update dependencies regularly
   - Test after website changes

## Development Notes

- The script is designed for headless execution
- Uses explicit waits for reliability
- Includes comprehensive error handling
- Returns structured JSON responses
