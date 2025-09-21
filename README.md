# Serverless URL Shortener

A serverless URL shortener built using AWS Lambda, API Gateway, DynamoDB, S3, CloudFront, and GitHub Actions for CI/CD.

## Features
- Serverless backend using AWS Lambda
- Short URL generation with random codes
- Persistent storage in DynamoDB
- Static frontend hosted on S3 + CloudFront
- Automated deployment pipeline with GitHub Actions

## Architecture
![Architecture Diagram](architecture.png)

## Tech Stack
- AWS Lambda
- API Gateway
- DynamoDB
- S3 + CloudFront
- GitHub Actions
- Python
- HTML, CSS, JS

## Deployment
1. Clone this repo
2. Create a DynamoDB table named `UrlShortenerTable`
3. Deploy the Lambda function
4. Configure API Gateway
5. Update `script.js` with API Gateway endpoint
