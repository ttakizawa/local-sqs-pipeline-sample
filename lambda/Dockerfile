# syntax=docker/dockerfile:1.2
FROM amazon/aws-lambda-python:3.8 as builder

RUN pip install -U wheel setuptools

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

FROM amazon/aws-lambda-python:3.8 as runner
# for timezone
RUN yum install -y tzdata
COPY --from=builder /var/lang/lib/python3.8/site-packages /var/lang/lib/python3.8/site-packages
WORKDIR ${LAMBDA_TASK_ROOT}
COPY . ${LAMBDA_TASK_ROOT}

COPY lambda_handler.py ./lambda_handler.py

CMD [ "lambda_handler.lambda_handler" ]
