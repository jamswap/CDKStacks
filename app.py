#!/usr/bin/env python3

from aws_cdk import cdk

from jamswap_cdk.jamswap_cdk_stack import JamswapCdkStack


app = cdk.App()
JamswapCdkStack(app, "jamswap-cdk-cdk-1")

app.run()
