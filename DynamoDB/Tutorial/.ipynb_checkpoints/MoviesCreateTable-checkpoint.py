{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import boto3\n",
    "\n",
    "dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url=\"http://localhost:8000\")\n",
    "\n",
    "\n",
    "table = dynamodb.create_table(\n",
    "    TableName='Movies',\n",
    "    KeySchema=[\n",
    "        {\n",
    "            'AttributeName': 'year',\n",
    "            'KeyType': 'HASH'  #Partition key\n",
    "        },\n",
    "        {\n",
    "            'AttributeName': 'title',\n",
    "            'KeyType': 'RANGE'  #Sort key\n",
    "        }\n",
    "    ],\n",
    "    AttributeDefinitions=[\n",
    "        {\n",
    "            'AttributeName': 'year',\n",
    "            'AttributeType': 'N'\n",
    "        },\n",
    "        {\n",
    "            'AttributeName': 'title',\n",
    "            'AttributeType': 'S'\n",
    "        },\n",
    "\n",
    "    ],\n",
    "    ProvisionedThroughput={\n",
    "        'ReadCapacityUnits': 10,\n",
    "        'WriteCapacityUnits': 10\n",
    "    }\n",
    ")\n",
    "\n",
    "print(\"Table status:\", table.table_status)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
