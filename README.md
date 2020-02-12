# AWS Lambda MongoDB Vpc Peering

This repository demonstrates how a Lambda Function needs to be configured to save items in MongoDB.
To connect to the MongoDB cluster vpc-peering is used.

## Prerequisites
* Python3 installed, version > 3.6
* aws cli installed: [instructions](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
* sam cli installed: [instructions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

## UPDATES
You need to update certain config values in this project to make it work for your own vpc!

In `template.yaml`: 
* update the environment variable that specifies the connection string to your own connection string.
    ```
      Environment:
        Variables:
          MONGODB_CONNECTION_STRING: mongodb+srv://<user>:<password>@<your-cluster>.mongodb.net/test?retryWrites=true&w=majority
    ```
* update the `VpcConfig` with your own vpc security group and subnet:
    ```shell script
      VpcConfig:
        SecurityGroupIds:
          - sg-08b12e8bdf431b849
        SubnetIds:
          - subnet-08a19d1a47914c5ac
    ```
## Deploy

From the root directory run `./deploy.sh`

This will:
* install the needed dependencies
* zip your code
* deploy the lambda function

Answer `y` on the input that is asked.

When you have deployed successfully you could change the last line of the script `sam deploy --guided` to `sam deploy`.
