                                  # Face_recognition_task_EC2-What-sAPP
-------------------------------------------------------------------------------------------------------



📌 When it recognize your face then -  

👉 It send mail to your mail id by writing this is face of your_name.  

👉 Second it send whatsapp message to your friend, it can be anything.  

📌 When it recognize second  face, it can be your friend or family members face. 

👉 Create EC2 instance in the AWS using CLI.  

👉 Create 5GB EBS volume and attach it to the instance. 

_______________________________________________________________________________________________________

Step 1 -> Train model to detect a face

_______________________________________________________________________________________________________

Here is a simple demo of the working model


![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/61656756/132636457-acc004a3-e5e4-4267-a75f-b7bd3ddcfdca.gif)

_______________________________________________________________________________________________________

Step 2 -> The next step is to launch ec2-instance and and send what'a app message when a face is recognized.

_______________________________________________________________________________________________________

![face_2](https://user-images.githubusercontent.com/61656756/132645279-d5277de4-b712-47a0-829b-857e16034f93.jpg)


I have used terraform to access and launch an ec2-instance.
_______________________________________________________________________________________________________

Step -3 After your ec2-instance is launched the code will send a message to your what's-app 

_______________________________________________________________________________________________________

![face_](https://user-images.githubusercontent.com/61656756/132645273-6dae1f6c-4230-4c06-9acb-15a032ad3945.jpg)


In order to send a what's-app message i have used twilio.rest library. Enter your phone number as well as your clients number.

_______________________________________________________________________________________________________

