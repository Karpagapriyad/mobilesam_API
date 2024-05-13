# mobilesam_API

## How to run the code without containersation

1. **Create a conda enviroinment and activate it**
  
    ```bash
    conda create -y python=3.9 --name mobilesam 
    conda activate mobilesam
    ```

2. **Install the Requirements**

    ```bash
    pip install -r requirements.txt
    ```

3. **To run FastAPI**

    ```bash
    uvicorn main:app --reload 
    ```

4. **To run stream-lit app**

    ```bash
    streamlit run app.py
    ```
Here I have created a webapp using streamlit for access of API.
If you run the stream lit comment it will automatically redirect you to the streamlit webpage page where you can use the API

## How to run the code containersation

1. **Install docker if it is not installed locally**
   Link to install docker - https://docs.docker.com/desktop/install/windows-install/ (For windows) intsall as per your OS
2. **To set up the container**
  ***To build the image:***
    ```bash
    docker build -t mobilesamapi .
    ```
 **To build container:**
    ```bash
    docker run -d --name sam -p 8000:8000 mobilesamapi
    ```
  **To check the conatiner running / all the containers:**
    ```bash
    sudo docker ps
    ```
    
    ```bash
    sudo docker ps -a
    ```
  **To start, stop, restart, and remove the container: use either container ID or container name**
    ```bash
    sudo docker start "container ID or container name"
    ```				
    
    ```bash
    sudo docker stop "container ID or container name"
    ```
    
    ```bash
    sudo docker restart "container ID or container name"
    ```
    
    ```bash
    sudo docker rm "container ID or container name"
    ```
**To access the service built the image and container and use  "http://0.0.0.0:8000/docs" to access API.**
    
   
   


      
