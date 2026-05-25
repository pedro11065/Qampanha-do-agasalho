FROM python:3.13

WORKDIR /app

COPY . .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV DOCKER_ENV=1  
# Define que o app está rodando no Docker

CMD ["python", "main.py"]

#docker build --no-cache -t qampanha_do_agasalho .

#docker save --output qampanha_do_agasalho.tar qampanha_do_agasalho
#scp -i "C:\Users\UXK\Downloads\qampanha_do_agasalho_ssh.pem" C:\Users\UXK\qampanha_do_agasalho.tar ubuntu@ec2-16-59-211-240.us-east-2.compute.amazonaws.com:/home/ubuntu/


# Script de conexão SSH (baseado nos comentários acima):
# - No Windows (PowerShell/CMD) usando a chave .pem:
#   scp -i "C:\Users\UXK\Downloads\qampanha_do_agasalho_ssh.pem" C:\Users\UXK\qampanha_do_agasalho.tar ubuntu@ec2-16-59-211-240.us-east-2.compute.amazonaws.com:/home/ubuntu/
#   ssh -i "C:\Users\UXK\Downloads\qampanha_do_agasalho_ssh.pem" ubuntu@ec2-16-59-211-240.us-east-2.compute.amazonaws.com
#
# Após conectar ao servidor EC2:
#   sudo docker load -i /home/ubuntu/qampanha_do_agasalho.tar
#   sudo docker run --rm -it -p 5000:5000 qampanha_do_agasalho
#
# Observações:
# - Ajuste os caminhos da chave e do arquivo .tar conforme necessário.
# - Garanta permissões corretas na chave: chmod 600 ~/.ssh/chave_qampanha_do_agasalho.pem


#docker ps
#docker stop <ID_OU_NOME>
#docker rm <ID_OU_NOME>
