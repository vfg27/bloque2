FROM python:3.5.7
RUN git clone https://github.com/vfg27/creativa2Bloque2
WORKDIR creativa2Bloque2
ENV GROUP_NUMBER 'Equipo47'
RUN pip3 install -r practica_creativa2-main/bookinfo/src/productpage/requirements.txt
EXPOSE 9080
CMD ["python3", "practica_creativa2-main/bookinfo/src/productpage/productpage_monolith.py", "80"]