# mobilesam_API

## How to run the code

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


      