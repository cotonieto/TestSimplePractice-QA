# TestSimplePractice-QA
Technical Assessment.

Hello! 

Dockerfile, Env and requeriments is part of the elements of the creation of Docker container 
I tried to create it but the build take forever and still investigating what is the cause of it 

below files pertaining to local solution, amd chromedriver needs to be downloaded and use Chrome 135.0.7049.41
requeriments.txt contains version of selenium and python to be used, and I added a folder with screenshot of the  test caases 
1 login_page_sample_Practice.py
2 create_client_samle_practice.py
3 verify_client-SimplePractice.py

for creation of client, below lines can be modified in create_client_samle_practice.py to add new clients 
input_first_name.send_keys("Carlos") ---- input_first_name.send_keys("Client name") 
input_last_name.send_keys("Urur") --------input_last_name.send_keys("Client Last Name")

for validation to see if new client was added in verify_client-SimplePractice.py the word that needs to be matched can be changed here 
if "Urur" in full_name: to if "Word to be search" in full_name:


 the rest of the files is my proposal to all the code be in Docker container 

 1 Login_simple_Practice_test.py
 2 Create_new_client_simple_practice.py
 3 Verify_Client_Simple_Practice
 4 Dockerfile
 5 Env.env
 6 README.md 
 7 requeriments.txt
 
thanks and best regards 

Edwin Cotonieto

