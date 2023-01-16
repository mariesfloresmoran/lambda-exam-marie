import json 
import os 
import mercadopago  
 
 
def lambda_handler(event, context): 
    sdk= mercadopago.SDK(os.environ["ACCESS_TOKEN"]) 
    bodyGet = event 
    
    payment_response = sdk.payment().create(bodyGet["paymentData"]) 
    payment = payment_response["response"] 
     
    preference_response = sdk.preference().create(bodyGet["productData"]) 
    preference = preference_response["response"] 
 
 
    return { 
        'statusCode': 200, 
        'body': json.dumps(preference) 
    }



    