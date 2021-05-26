FROM python:3.9.5

ENV ROOT_FOLDER="/github/workspace"
ENV OPERATION="IS_COMPATIBLE"
ENV COMPATIBILITY_FILE="./compatibility.json"
ENV COMPONENT_ONE="C_1"
ENV COMPONENT_TWO="C_2"
ENV VERSION_ONE="V_1"
ENV VERSION_TWO="V_2"
ENV COMPATIBLE="false"

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["/usr/src/app/check-compatibility.py"]

ENTRYPOINT ["python3"]