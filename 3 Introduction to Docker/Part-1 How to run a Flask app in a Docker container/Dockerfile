FROM python:3.13.5
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]

## kita membuat image dengan docker file, line demi line:
# versi python
# port yang digunakan
# pindah ke app folder
# instal flask
# menyalin salinan isi dirictory saat ini ke directory saat ini, yaitu /app
# list dengan 4 string, dan setiap string adala satu bagian perintah (command) yang ingin kita jalankan. Apa yang dilakukan adalah memungkinan external clients ke container untuk membuat request ke flask app yang bejralan di container
# kita memiliki Dockerfile dan sekarnag yang kita lakukan menjalankan pada terminal : "docker build -t rest-apis-flask-python."

# menjalankan docker image lewat terminal: "docker run -p 5005:5000 rest-apis-flask-ptyhon"
# menjalankan docker image lewat terminal tpi dilatar belakang: "docker run -dp 5005:5000 rest-apis-flask-ptyhon"