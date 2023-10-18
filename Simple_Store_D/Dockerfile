FROM python:3

WORKDIR /home/src 

RUN apt-get update && apt-get install -y netcat-traditional

COPY requirements.txt ./ 

RUN pip install --no-cache-dir -r requirements.txt 

COPY ./entrypoint.sh . 

RUN sed -i 's/\r$//g' /home/src/entrypoint.sh 
RUN chmod +x /home/src/entrypoint.sh 

COPY . .

ENTRYPOINT ["/home/src/entrypoint.sh"]