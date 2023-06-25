import boto3
mysns = boto3.client("sns")

def lw(x, y):

  mysns.publish(
    TopicArn='arn:aws:sns:ap-south-1:351345331205:myeventopic',
    Message='something is uploaded',
    Subject='I got new doc in s3 bucket',
  
  )
  print("Hey i am sachin Rajput from s3 bucket..... NOw I am going tO Call sns....")
