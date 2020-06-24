FROM python:3.8.3
COPY . /build/
WORKDIR /build/
RUN pip install mkdocs
EXPOSE 8080
CMD ["mkdocs", "serve"]
