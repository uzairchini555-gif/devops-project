FROM python:3.9
WORKDIR /app
# Copy dependency file first (best practise for caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy project files 
COPY . .
#CI/CD build metadata (will come from Github Actions)
ARG VERSION 
ARG COMMIT 
ENV APP_VERSION=$VERSION 
ENV APP_COMMIT=$COMMIT 
HEALTHCHECK CMD curl --fail http://localhost:5000/ || exit 1
EXPOSE 5000
CMD ["python", "app.py"]

