''' 
    Input: 
    - 3 inputs: 
        - Moxfield curl
        - Text boxes 
        - Files
    - Not storing files in S3, but using S3 to process

    Validation: 
    - Front-end for each type
    - Back-end for each type
    - Limit to 100 cards? 
    - Class validation    

    Logging: 
    - Log invocation
    - Errors
    - Success

    General: 
    - If input from lambda, how to handle 
    - Let users provide parameters to the call
    - Output list with modifiers

    Big Things: 
    - Convert code to work with lambda
        - Don't take files one at a time as user input (update arguments)
        - Validation 
        - How to send file in lambda event
        - How to see what kind of event the lambda is
    - Host and run code on lambda
    - Make front-end 
        - Front-end validation
            - Up to 100 cards (Limit to commander) 
            - Check filesize 
            - Check file format
            - Check file contents
            - Input Validation
            - Validation before sending to lambda
        - Back-end validation 
            - Match to front-end 
        - Square up the possible inputs
        - Handler
        - Authorizer
        - Events
            - Type of invent dictates how the lambda runs
    - Deploy to some CDN / Host it somewhere

    Testing: 
    - eventually

    Gold Plates: 
    - Make printable outputs of changes in sleevable size
    - Save to file    properties: 
            - card_name
            - quantity (can be negative)
            - change_type as add, remove, or modify
                - negative quantity must be a remove or modify
                - positive quantity must be an add or modify

'''